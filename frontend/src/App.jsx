import React, { useMemo, useState } from "react";
import AssessmentForm from "./components/AssessmentForm.jsx";
import AssessmentResults from "./components/AssessmentResults.jsx";
import "./styles/main.css";

const translations = {
  en: {
    title: "Financial Health Assessment Tool",
    subtitle: "AI-powered insights for SME financial decisions",
    languageLabel: "Language",
  },
  hi: {
    title: "वित्तीय स्वास्थ्य आकलन उपकरण",
    subtitle: "एसएमई वित्तीय निर्णयों के लिए एआई आधारित अंतर्दृष्टि",
    languageLabel: "भाषा",
  },
};

export default function App() {
  const [language, setLanguage] = useState("en");
  const [assessment, setAssessment] = useState(null);
  const copy = useMemo(() => translations[language], [language]);

  return (
    <div className="app">
      <header className="app__header">
        <div>
          <h1>{copy.title}</h1>
          <p>{copy.subtitle}</p>
        </div>
        <label className="app__language">
          {copy.languageLabel}
          <select value={language} onChange={(event) => setLanguage(event.target.value)}>
            <option value="en">English</option>
            <option value="hi">हिंदी</option>
          </select>
        </label>
      </header>
      <main className="app__main">
        <AssessmentForm onAssess={setAssessment} language={language} />
        <AssessmentResults assessment={assessment} />
      </main>
    </div>
  );
}
