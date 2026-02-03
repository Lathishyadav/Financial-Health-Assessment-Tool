import pandas as pd


def _safe_divide(numerator: float, denominator: float) -> float:
    return numerator / (denominator if denominator else 1)


def _localize(text: str, language: str) -> str:
    translations = {
        "en": {},
        "hi": {
            "Risk Score": "जोखिम स्कोर",
            "Credit Score": "क्रेडिट स्कोर",
            "Strong": "मजबूत",
            "Moderate": "मध्यम",
            "High Risk": "उच्च जोखिम",
        },
    }
    if language not in translations:
        return text
    return translations[language].get(text, text)


def assess_financial_health(payload: dict) -> dict:
    data = {
        "revenue": [payload["revenue"]],
        "prior_revenue": [payload.get("prior_revenue", 0)],
        "expenses": [payload["expenses"]],
        "cogs": [payload.get("cogs", 0)],
        "receivables": [payload["receivables"]],
        "payables": [payload["payables"]],
        "inventory": [payload["inventory"]],
        "debt": [payload["debt"]],
        "cash_on_hand": [payload["cash_on_hand"]],
        "monthly_burn": [payload.get("monthly_burn", 0)],
        "tax_liability": [payload.get("tax_liability", 0)],
        "deductions": [payload.get("deductions", 0)],
    }
    df = pd.DataFrame(data)

    gross_margin = _safe_divide(df["revenue"] - df["cogs"], df["revenue"])
    net_margin = _safe_divide(df["revenue"] - df["expenses"], df["revenue"])
    revenue_growth = _safe_divide(df["revenue"] - df["prior_revenue"], df["prior_revenue"])
    liquidity_ratio = _safe_divide(df["cash_on_hand"] + df["receivables"], df["payables"])
    leverage_ratio = _safe_divide(df["debt"], df["revenue"])
    inventory_turnover = _safe_divide(df["revenue"], df["inventory"])
    working_capital_cycle = _safe_divide(df["receivables"] + df["inventory"] - df["payables"], df["revenue"])
    dscr = _safe_divide(df["revenue"] - df["expenses"], df["debt"] + 1)
    tax_coverage = _safe_divide(df["deductions"], df["tax_liability"] + 1)

    gross_margin_value = round(float(gross_margin.iloc[0]) * 100, 2)
    net_margin_value = round(float(net_margin.iloc[0]) * 100, 2)
    growth_value = round(float(revenue_growth.iloc[0]) * 100, 2)
    liquidity_value = round(float(liquidity_ratio.iloc[0]), 2)
    leverage_value = round(float(leverage_ratio.iloc[0]), 2)
    inventory_turn_value = round(float(inventory_turnover.iloc[0]), 2)
    wcc_value = round(float(working_capital_cycle.iloc[0]) * 100, 2)
    dscr_value = round(float(dscr.iloc[0]), 2)
    tax_coverage_value = round(float(tax_coverage.iloc[0]), 2)

    liquidity_score = max(0.0, min(100.0, 100 - (liquidity_value < 1.2) * 25 + liquidity_value * 5))
    profitability_score = max(0.0, min(100.0, gross_margin_value * 0.6 + net_margin_value * 0.4))
    solvency_score = max(0.0, min(100.0, 100 - leverage_value * 80))
    efficiency_score = max(0.0, min(100.0, inventory_turn_value * 8 + (100 - abs(wcc_value))))
    compliance_score = max(0.0, min(100.0, tax_coverage_value * 40 + 60))

    component_scores = [
        {"name": "Liquidity", "score": round(liquidity_score, 2), "insight": "Measures short-term buffer."},
        {"name": "Profitability", "score": round(profitability_score, 2), "insight": "Margin strength and resilience."},
        {"name": "Solvency", "score": round(solvency_score, 2), "insight": "Debt capacity and leverage."},
        {"name": "Efficiency", "score": round(efficiency_score, 2), "insight": "Working capital effectiveness."},
        {"name": "Compliance", "score": round(compliance_score, 2), "insight": "Tax readiness and coverage."},
    ]

    risk_score = round(100 - sum(item["score"] for item in component_scores) / len(component_scores), 2)
    credit_score = round(sum(item["score"] for item in component_scores) / len(component_scores), 2)

    health_label = "Strong" if risk_score < 35 else "Moderate" if risk_score < 65 else "High Risk"
    risk_alerts = []
    if liquidity_value < 1.2:
        risk_alerts.append("Low liquidity coverage detected.")
    if leverage_value > 0.6:
        risk_alerts.append("High leverage exposure relative to revenue.")
    if growth_value < 0:
        risk_alerts.append("Revenue contraction compared to prior period.")
    if tax_coverage_value < 0.5:
        risk_alerts.append("Tax coverage appears below optimal levels.")

    recommendations = []
    if gross_margin_value < 25:
        recommendations.append("Improve gross margin through supplier renegotiation or pricing review.")
    if liquidity_value < 1.2:
        recommendations.append("Increase liquidity by accelerating collections or extending payment terms.")
    if leverage_value > 0.6:
        recommendations.append("Reduce leverage with debt restructuring or equity infusion.")
    if dscr_value < 1.1:
        recommendations.append("Boost operating surplus to improve debt-service coverage.")
    if not recommendations:
        recommendations.append("Maintain current discipline and invest in growth initiatives.")

    metrics = [
        {"name": "Gross Margin (%)", "value": gross_margin_value, "insight": "Measures profitability after direct costs."},
        {"name": "Net Margin (%)", "value": net_margin_value, "insight": "Tracks profit after operating expenses."},
        {"name": "Revenue Growth (%)", "value": growth_value, "insight": "Compares revenue to prior period."},
        {"name": "Liquidity Ratio", "value": liquidity_value, "insight": "Ability to cover short-term obligations."},
        {"name": "Leverage Ratio", "value": leverage_value, "insight": "Debt load relative to revenue."},
        {"name": "Inventory Turnover", "value": inventory_turn_value, "insight": "Inventory efficiency signal."},
        {"name": "DSCR", "value": dscr_value, "insight": "Debt service coverage ratio."},
    ]

    product_recommendations = [
        {
            "name": "Working Capital Loan",
            "rationale": "Suitable if liquidity is below target and receivables are high.",
        },
        {
            "name": "Invoice Discounting",
            "rationale": "Releases cash tied in receivables to improve cash flow cycle.",
        },
    ]

    benchmark_summary = (
        f"{payload['industry']} peers typically show gross margins of 28-35%. Your current gross margin is "
        f"{gross_margin_value}%, indicating {'room to improve' if gross_margin_value < 28 else 'healthy alignment'}."
    )

    forecast_summary = (
        f"Projected 6-month revenue trend is {('stable' if growth_value >= 0 else 'softening')} with an estimated "
        f"monthly burn of {payload.get('monthly_burn', 0):,.0f}."
    )

    narrative = (
        f"{payload['business_name']} shows a {_localize(health_label, payload.get('language', 'en')).lower()} profile "
        f"with a risk score of {round(risk_score, 1)}. Liquidity and leverage trends suggest targeted working "
        f"capital and debt optimization steps."
    )

    return {
        "risk_score": round(float(risk_score), 2),
        "credit_score": round(float(credit_score), 2),
        "health_label": _localize(health_label, payload.get("language", "en")),
        "metrics": metrics,
        "component_scores": component_scores,
        "risk_alerts": risk_alerts,
        "product_recommendations": product_recommendations,
        "benchmark_summary": benchmark_summary,
        "forecast_summary": forecast_summary,
        "recommendations": recommendations,
        "narrative": narrative,
    }
