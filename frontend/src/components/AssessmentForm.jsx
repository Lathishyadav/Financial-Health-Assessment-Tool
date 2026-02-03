import React, { useState } from "react";

const defaultValues = {
  business_name: "Apex Traders",
  industry: "Retail",
  region: "Maharashtra",
  revenue: 1250000,
  prior_revenue: 1180000,
  expenses: 860000,
  cogs: 620000,
  receivables: 180000,
  payables: 140000,
  inventory: 220000,
  debt: 350000,
  cash_on_hand: 90000,
  monthly_burn: 25000,
  tax_liability: 52000,
  deductions: 18000,
};

export default function AssessmentForm({ onAssess, language }) {
  const [formValues, setFormValues] = useState(defaultValues);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormValues((prev) => ({
      ...prev,
      [name]: name === "business_name" || name === "industry" || name === "region" ? value : Number(value),
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError("");

    const payload = { ...formValues, language };
    try {
      const response = await fetch("/api/assess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error("Unable to generate assessment. Please try again.");
      }

      const data = await response.json();
      onAssess(data);
    } catch (err) {
      setError(err.message || "Unexpected error.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h2>Business Snapshot</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Business Name
          <input name="business_name" value={formValues.business_name} onChange={handleChange} />
        </label>
        <label>
          Industry
          <input name="industry" value={formValues.industry} onChange={handleChange} />
        </label>
        <label>
          Region
          <input name="region" value={formValues.region} onChange={handleChange} />
        </label>
        <label>
          Revenue
          <input name="revenue" type="number" value={formValues.revenue} onChange={handleChange} />
        </label>
        <label>
          Prior Revenue
          <input name="prior_revenue" type="number" value={formValues.prior_revenue} onChange={handleChange} />
        </label>
        <label>
          Expenses
          <input name="expenses" type="number" value={formValues.expenses} onChange={handleChange} />
        </label>
        <label>
          COGS
          <input name="cogs" type="number" value={formValues.cogs} onChange={handleChange} />
        </label>
        <label>
          Receivables
          <input name="receivables" type="number" value={formValues.receivables} onChange={handleChange} />
        </label>
        <label>
          Payables
          <input name="payables" type="number" value={formValues.payables} onChange={handleChange} />
        </label>
        <label>
          Inventory
          <input name="inventory" type="number" value={formValues.inventory} onChange={handleChange} />
        </label>
        <label>
          Debt
          <input name="debt" type="number" value={formValues.debt} onChange={handleChange} />
        </label>
        <label>
          Cash on Hand
          <input name="cash_on_hand" type="number" value={formValues.cash_on_hand} onChange={handleChange} />
        </label>
        <label>
          Monthly Burn
          <input name="monthly_burn" type="number" value={formValues.monthly_burn} onChange={handleChange} />
        </label>
        <label>
          Tax Liability
          <input name="tax_liability" type="number" value={formValues.tax_liability} onChange={handleChange} />
        </label>
        <label>
          Deductions
          <input name="deductions" type="number" value={formValues.deductions} onChange={handleChange} />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? "Assessing..." : "Generate Assessment"}
        </button>
        {error ? <p className="form__error">{error}</p> : null}
      </form>
    </section>
  );
}
