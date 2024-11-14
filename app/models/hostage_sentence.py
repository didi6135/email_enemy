from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from app.models import Base


class HostageSentence(Base):
    __tablename__ = 'hostage_sentences'

    id = Column(Integer, primary_key=True, index=True)
    user_detail_id = Column(Integer, ForeignKey('user_details.id', ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)
    content = Column(Text, nullable=True)

    # Relationship to UserDetail (many-to-one)
    user_detail = relationship("UserDetail", back_populates="hostage_sentences")
