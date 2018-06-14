from freya import db

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Float, DateTime, Boolean
from sqlalchemy import BigInteger, SmallInteger

Base = db.Model


class IridiumPacket(Base):
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    sdr_reference = Column(Integer)
    imai = Column(String(length=100))
    session_status = Column(SmallInteger)
    momsn = Column(Integer)
    mtmsn = Column(Integer)
    time_of_session = Column(DateTime)

    #location information
    indicator = Column(SmallInteger)
    latitude = Column(Float)
    lohgitude = Column(Float)
    cep_radius = Column(Integer)

    __tablename__ = "Iridium_packets"

    ref_freya_packets = relationship("FreyaPacket", back_populates = "ref_iridium_packet")


class FreyaPacket(Base):
    id = Column(BigInteger, primary_key=True, nullable=False)

    iridium_packet_id = Column(ForeignKey(IridiumPacket.id), nullable=False)

    flag = Column(SmallInteger)
    time = Column(BigInteger)

    bmp_press = Column(Float)
    bmp_temp = Column(Float)
    dc_temp = Column(Float)

    accx = Column(Float)
    accy = Column(Float)
    accz = Column(Float)

    cdm_conc = Column(BigInteger)
    mq7_conc = Column(BigInteger)
    geiger_ticks = Column(BigInteger)

    latitude = Column(Float)
    longitude = Column(Float)
    has_fix = Column(Boolean)

    __tablename__ = "Freya_packets"

    ref_freya_packets = relationship(IridiumPacket, back_populates="ref_iridium_packet")







