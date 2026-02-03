from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.db import engine, get_db
from app.models import Base
from app.schemas import AssessmentResponse, FinancialInput
from app.services.analysis import assess_financial_health

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Health Assessment Tool", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


@app.post("/assess", response_model=AssessmentResponse)
def assess_financials(payload: FinancialInput, db: Session = Depends(get_db)):
    _ = db
    return assess_financial_health(payload.model_dump())
