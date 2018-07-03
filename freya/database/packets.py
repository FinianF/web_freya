from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Float, DateTime, Boolean
from sqlalchemy import BigInteger, SmallInteger
from datetime import datetime
from cmath import e

from freya.database import db
from freya.database.node import FreyaNode

Base = db.Model

class IridiumPacket(Base):
    __tablename__ = "Iridium_packets"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    
    freya_node_imei = Column(ForeignKey(FreyaNode.imei), nullable=False)

    cdr_reference = Column(Integer)
    session_status = Column(SmallInteger)
    momsn = Column(Integer)
    mtmsn = Column(Integer)
    time_of_session = Column(DateTime)

    indicator = Column(SmallInteger)
    latitude = Column(Float)
    longitude = Column(Float)
    cep_radius = Column(Integer)

    ref_freya_packets = relationship("FreyaPacket", back_populates="ref_iridium_packet")
    
    ref_freya_node = relationship("FreyaNode", back_populates="ref_iridium_packets")
    
    def __init__(self, header, loc):
        self.cdr_reference = header['CDRReference']
        self.session_status = header['SessionStatus']
        self.freya_node_imei = header['IMEI']
        self.momsn = header['MOMSN']
        self.mtmsn = header['MTMSN']
        self.time_of_session = datetime.utcfromtimestamp(header['TimeOfSession'])

        self.indicator = loc['Indicator']
        self.latitude = loc['LatitudeDegrees']
        self.longitude = loc['LongitudeDegrees']
        self.cep_radius = loc['CEPRadius']
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get():
        pass


def gps_convert(raw_data):
    raw_data = str(raw_data)
    data_degree = raw_data[:2] + "."
    data_minute = int(raw_data[3:]) // 60
    convert_data = float(data_degree + str(data_minute))

    return convert_data
    

class FreyaPacket(Base):
    __tablename__ = "Freya_packets"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    iridium_packet_id = Column(ForeignKey(IridiumPacket.id), nullable=False)

    flag = Column(SmallInteger)
    time = Column(BigInteger)

    bmp_press = Column(Float)
    bmp_temp = Column(Float)
    ds_temp = Column(Float)

    accx = Column(Float)
    accy = Column(Float)
    accz = Column(Float)

    cdm_conc = Column(BigInteger)
    mq7_conc = Column(BigInteger)
    geiger_ticks = Column(BigInteger)

    height = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    has_fix = Column(Boolean)
    
    radiation = Column(Float)

    ref_iridium_packet = relationship('IridiumPacket', back_populates="ref_freya_packets")
    
    def __init__(self, pack, irid):
        self.ref_iridium_packet = irid

        self.flag = pack['Flag']
        self.time = pack['Time']

        self.bmp_press = pack['BMPPress']
        self.bmp_temp = pack['BMPTemp'] / 100
        self.ds_temp = pack['DSTemp'] / 16

        self.accx = pack['X']
        self.accy = pack['Y']
        self.accz = pack['Z']

        self.cdm_conc = pack['CDMConc']
        self.mq7_conc = 3.027 * e**(1.0698 * (5 / 1023 * pack['MQ7Conc']))
        self.geiger_ticks = pack['GeigerTicks']
        self.height = pack['Height']
        self.has_fix = pack['HasFix']

        pre_lat = str(pack['Latitude'] / 100).split(".")
        pre_lon = str(pack['Longitude'] / 100).split(".")
        
        self.latitude = float(pre_lat[0] + "." + str(int(pre_lat[1]) // 60))
        self.longitude = float(pre_lon[0] + "." + str(int(pre_lon[1]) // 60))
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def to_dict(self):
        return {"time": self.time,
                "lon": self.longitude,
                "lat": self.latitude,
                "co": self.mq7_conc,
                "co2": self.cdm_conc,
                "press": self.bmp_press,
                "temp": self.bmp_temp,
                "radiaion": self.radiation,
                "formated": "Координаты: {0}, {1}<br>Давление: {2} мм рт. ст.<br>" \
                            "Температура: {3} °C<br> Концентрация CO2: {4} ppm<br>" \
                            "Концентрация CO: {5} ppm<br>Уровень радиации: {6} мкР/ч".format(
                            self.latitude, self.longitude, self.bmp_press, 
                            self.bmp_temp, self.cdm_conc, self.mq7_conc, self.radiation)
        }
        
    def calc_radiation(self):
        try:
            node = self.ref_iridium_packet.ref_freya_node
            irips = node.ref_iridium_packets
            freps = list()
            
            for irip in irips:
                freps += irip.ref_freya_packets
                
            res = freps[0]
            for p in freps:
                if p.id > res.id and p.id < self.id: res = p
                
            if self == res: raise
            dtime, dticks = self.time - res.time, self.geiger_ticks - res.geiger_ticks
        except:
            dtime, dticks = self.time, self.geiger_ticks
        self.radiation = (dticks / 78) / dtime * 3600







