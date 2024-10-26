// src/Calculator.js
import React, { useState } from "react";
import { calculateNPI } from "./api";
import "./Calculator.css";

const Calculator = () => {
  const [expression, setExpression] = useState("");
  const [result, setResult] = useState(null);
  const [message, setMessage] = useState("");
  const [isCorrect, setIsCorrect] = useState(null); // true, false or null for no result

  const handleCalculate = async () => {
    try {
      const calcResult = await calculateNPI(expression);
      setResult(calcResult);
      setIsCorrect(true);
      setMessage("🎉 Félicitations, ta réponse est exacte!");
    } catch (error) {
      console.error("Erreur lors du calcul :", error);
      setResult("Erreur");
      setIsCorrect(false);
      setMessage("😢 Dommage, il y a une erreur dans ton calcul.");
    }
  };

  return (
    <div className="calculator-container">
      <h2>Calculatrice NPI</h2>
      <input
        type="text"
        className="calculator-input"
        value={expression}
        onChange={(e) => setExpression(e.target.value)}
        placeholder="Entrez un calcul NPI à faire"
      />
      <button onClick={handleCalculate} className="calculator-button">
        Calculer
      </button>
      {result !== null && (
        <div className="result-container">
          <div className={`result-message ${isCorrect ? "success" : "error"}`}>
            {message}
          </div>
          <div className="result-value">
            Résultat: <strong>{result}</strong>
          </div>
        </div>
      )}
    </div>
  );
};

export default Calculator;
