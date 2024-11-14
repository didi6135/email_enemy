from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base

class UserDetail(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), nullable=True)
    ip_address = Column(String(15), nullable=True)

    location_id = Column(Integer, ForeignKey('locations.id', ondelete="SET NULL"), nullable=True)
    device_id = Column(Integer, ForeignKey('device_info.id', ondelete="SET NULL"), nullable=True)

    location = relationship("Location", back_populates="user_detail")
    device = relationship("DeviceInfo", back_populates="user_detail")

    explosive_sentences = relationship("ExplosiveSentence", back_populates="user_detail", cascade="all, delete-orphan")
    hostage_sentences = relationship("HostageSentence", back_populates="user_detail", cascade="all, delete-orphan")