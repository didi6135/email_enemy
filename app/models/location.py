from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

from app.models import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    city = Column(String(100), nullable=True)
    country = Column(String(2), nullable=True)

    user_detail = relationship("UserDetail", back_populates="location")