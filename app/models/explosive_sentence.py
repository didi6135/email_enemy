from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models import Base


class ExplosiveSentence(Base):
    __tablename__ = 'explosive_sentences'

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, ForeignKey('emails.id', ondelete="CASCADE"))
    content = Column(Text, nullable=True)

    # Relationship to Email (many-to-one)
    email = relationship("Email", back_populates="explosive_sentences")