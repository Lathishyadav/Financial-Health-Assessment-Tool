import React from "react";

export default function AssessmentResults({ assessment }) {
  if (!assessment) {
    return (
      <section className="card card--empty">
        <h2>Assessment Output</h2>
        <p>Fill in the form to generate creditworthiness and risk insights.</p>
      </section>
    );
  }

  return (
    <section className="card">
      <h2>Assessment Output</h2>
      <div className="results__summary">
        <div>
          <h3>Risk Score</h3>
          <p className="results__score">{assessment.risk_score}</p>
        </div>
        <div>
          <h3>Credit Score</h3>
          <p className="results__score">{assessment.credit_score}</p>
        </div>
        <div>
          <h3>Health Label</h3>
          <p className="results__label">{assessment.health_label}</p>
        </div>
      </div>
      <div className="results__grid">
        <div>
          <h4>Component Scores</h4>
          <ul>
            {assessment.component_scores.map((component) => (
              <li key={component.name}>
                <strong>{component.name}:</strong> {component.score} <span>{component.insight}</span>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4>Risk Alerts</h4>
          <ul>
            {assessment.risk_alerts.length ? (
              assessment.risk_alerts.map((alert) => <li key={alert}>{alert}</li>)
            ) : (
              <li>No critical alerts detected.</li>
            )}
          </ul>
        </div>
      </div>
      <div className="results__grid">
        <div>
          <h4>Key Metrics</h4>
          <ul>
            {assessment.metrics.map((metric) => (
              <li key={metric.name}>
                <strong>{metric.name}:</strong> {metric.value} <span>{metric.insight}</span>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4>Recommendations</h4>
          <ul>
            {assessment.recommendations.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
      <div className="results__grid">
        <div>
          <h4>Product Recommendations</h4>
          <ul>
            {assessment.product_recommendations.map((product) => (
              <li key={product.name}>
                <strong>{product.name}:</strong> <span>{product.rationale}</span>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4>Benchmarks & Forecast</h4>
          <ul>
            <li>{assessment.benchmark_summary}</li>
            <li>{assessment.forecast_summary}</li>
          </ul>
        </div>
      </div>
      <div className="results__narrative">
        <h4>Narrative Summary</h4>
        <p>{assessment.narrative}</p>
      </div>
    </section>
  );
}
