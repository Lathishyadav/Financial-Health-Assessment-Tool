# Financial Health Assessment Tool

A full-stack platform concept and working prototype that helps SMEs understand financial health, creditworthiness, and risk exposure with AI-assisted insights. It combines data ingestion, analytics, and clear visualizations for non-finance business owners.

## What’s Included
- **Backend API** (FastAPI + pandas) to score risk, creditworthiness, and generate recommendations.
- **Frontend UI** (React + Vite) for data entry, multilingual toggles, and dashboard output.
- **PostgreSQL** for secure storage (via Docker Compose).
- **Security-first defaults** including TLS-ready architecture, role-based access plans, and encryption-at-rest guidance.

## High-Level Architecture (Logical)
```
React Frontend
   |
FastAPI Gateway
   |
Data Processing (pandas)
   |
AI Intelligence Layer (GPT-5 ready)
   |
PostgreSQL (encrypted storage)
   |
Integrations: Banking API + GST API
```

## Quick Start (Local)

### 1) Backend API
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3) Docker Compose (API + DB)
```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`, and the UI at `http://localhost:5173`.

## API Overview
- `GET /health` → service status
- `POST /assess` → generate assessment insights from financial input data

Sample payload:
```json
{
  "business_name": "Apex Traders",
  "industry": "Retail",
  "region": "Maharashtra",
  "language": "en",
  "revenue": 1250000,
  "prior_revenue": 1180000,
  "expenses": 860000,
  "cogs": 620000,
  "receivables": 180000,
  "payables": 140000,
  "inventory": 220000,
  "debt": 350000,
  "cash_on_hand": 90000,
  "monthly_burn": 25000,
  "tax_liability": 52000,
  "deductions": 18000
}
```

## Core Capabilities
- **Creditworthiness evaluation** with risk scoring based on revenue stability, leverage, and payment behavior.
- **Financial risk detection** for cash flow gaps, overdue receivables, high-cost debt, and inventory inefficiencies.
- **Cost optimization guidance** through spend categorization and variance analysis.
- **Product recommendations** from banks/NBFCs aligned to working capital needs and repayment capacity.

## Core Modules
- **Data ingestion**: CSV/XLSX/PDF (text exports), optional banking + GST APIs, schema validation, and auto-categorization.
- **Financial analysis engine**: growth, margins, burn rate, working capital cycle, AR/AP aging, DSCR, and inventory turnover.
- **AI intelligence layer**: plain-language insights, anomaly detection, multilingual narratives, and report summaries.

## Advanced Features (Roadmap)
- Automated bookkeeping assistance and reconciliation.
- Tax compliance checks for deductions and filing metadata.
- Financial forecasting and scenario planning.
- Working capital optimization recommendations.
- Integration with GST returns and up to two banking/payment APIs.
- Industry-specific benchmarking.
- Investor-ready financial reports.
- Multilingual output (English + Hindi/Regional).

## Security & Compliance Principles
- Encryption for all financial data at rest and in transit.
- Strict access controls and least-privilege permissions.
- Compliance-ready logging and retention policies.

## Next Steps
- Extend ingestion to CSV/XLSX/PDF extracts.
- Add authentication and audit logging.
- Build industry benchmarking datasets.
- Expand multilingual glossary coverage.
