from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base

class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), nullable=True)
    ip_address = Column(String(15), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    location_id = Column(Integer, ForeignKey('locations.id', ondelete="SET NULL"), nullable=True)
    device_id = Column(Integer, ForeignKey('device_info.id', ondelete="SET NULL"), nullable=True)

    # Relationships
    location = relationship("Location", back_populates="emails")
    device = relationship("DeviceInfo", back_populates="emails")
    explosive_sentences = relationship("ExplosiveSentence", back_populates="email", cascade="all, delete-orphan")
    hostage_sentences = relationship("HostageSentence", back_populates="email", cascade="all, delete-orphan")
