from pydantic import BaseModel, Field


class FinancialInput(BaseModel):
    business_name: str = Field(..., examples=["Apex Traders"])
    industry: str = Field(..., examples=["Retail"])
    region: str = Field(..., examples=["Maharashtra"])
    language: str = Field("en", examples=["en", "hi"])
    revenue: float = Field(..., ge=0)
    prior_revenue: float = Field(0, ge=0)
    expenses: float = Field(..., ge=0)
    cogs: float = Field(0, ge=0)
    receivables: float = Field(..., ge=0)
    payables: float = Field(..., ge=0)
    inventory: float = Field(..., ge=0)
    debt: float = Field(..., ge=0)
    cash_on_hand: float = Field(..., ge=0)
    monthly_burn: float = Field(0, ge=0)
    tax_liability: float = Field(0, ge=0)
    deductions: float = Field(0, ge=0)


class AssessmentMetric(BaseModel):
    name: str
    value: float
    insight: str


class ComponentScore(BaseModel):
    name: str
    score: float
    insight: str


class ProductRecommendation(BaseModel):
    name: str
    rationale: str


class AssessmentResponse(BaseModel):
    risk_score: float
    credit_score: float
    health_label: str
    metrics: list[AssessmentMetric]
    component_scores: list[ComponentScore]
    risk_alerts: list[str]
    product_recommendations: list[ProductRecommendation]
    benchmark_summary: str
    forecast_summary: str
    recommendations: list[str]
    narrative: str
