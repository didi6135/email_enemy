# app/models/device_info.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models import Base


class DeviceInfo(Base):
    __tablename__ = 'device_info'

    id = Column(Integer, primary_key=True, index=True)
    browser = Column(String(255), nullable=True)
    os = Column(String(50), nullable=True)
    device_id = Column(String(255), unique=True, nullable=False)

    # Relationship to UserDetail
    user_detail = relationship("UserDetail", back_populates="device")
