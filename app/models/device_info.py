from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from app.models import Base


class DeviceInfo(Base):
    __tablename__ = 'device_info'

    id = Column(Integer, primary_key=True, index=True)
    browser = Column(String(255), nullable=True)
    os = Column(String(50), nullable=True)
    device_id = Column(String(255), unique=True, nullable=False)

    emails = relationship("Email", back_populates="device")