from datetime import datetime
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.models import Base


class ExplosiveSentence(Base):
    __tablename__ = 'explosive_sentences'

    id = Column(Integer, primary_key=True, index=True)
    user_detail_id = Column(Integer, ForeignKey('user_details.id', ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)
    content = Column(Text, nullable=True)

    user_detail = relationship("UserDetail", back_populates="explosive_sentences")
