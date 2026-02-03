from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    industry = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class FinancialAssessment(Base):
    __tablename__ = "financial_assessments"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, nullable=False)
    risk_score = Column(Float, nullable=False)
    credit_score = Column(Float, nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
