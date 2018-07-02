from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import String

from freya.database import db

Base = db.Model

class FreyaNode(Base):
    imei = Column(String(30), primary_key=True, autoincrement=False)
    
    ref_iridium_packets = relationship("IridiumPacket", back_populates="ref_freya_node")
    
    def __init__(self, imei):
        self.imei = imei
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get(imei=None):
        if imei: return FreyaNode.query.get(imei)
        return FreyaNode.query.all()
