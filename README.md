# Compass: EVProject

Compass is a lightweight web application that helps electric vehicle owners and buyers make better decisions by combining data tracking, simple ML-driven insights, and a clean web interface.

Compass focuses on three core questions:
1. How healthy is my EV battery over time?
2. Where should I charge right now?
3. Which EV should I buy given my needs and budget?

---

## ✨ Features

### 🔋 Battery Tracker
- Track vehicles and battery snapshots over time
- Store odometer, full-charge range, and state-of-health (SoH)
- Estimate battery degradation trends
- Predict near-term battery health using baseline models (with ML hooks)

### ⚡ Charge Finder
- List nearby charging stations
- Rank stations based on:
  - Distance
  - Charging power compatibility
  - Reliability proxy
- Designed to evolve from heuristics → ML ranking models

### 🚗 EVs to Buy
- Recommend EVs based on:
  - Budget
  - Minimum driving range
  - Charging speed
  - Cargo and drivetrain preferences
- Transparent scoring with human-readable explanations

---

## 🧠 Machine Learning Approach

Compass is ML-ready but not ML-dependent.

- Baseline logic works without trained models
- PyTorch models are trained separately using Jupyter notebooks
- Models are exported as TorchScript artifacts
- Backend loads ML models if available, otherwise falls back to heuristics

This ensures robustness, explainability, and easy iteration.

---

## 🏗️ Architecture

- Frontend: Static HTML/CSS/JS (`index.html`)
- Backend: FastAPI (Python)
- Database: PostgreSQL
- ML: PyTorch (training via `.ipynb`)
- Hosting: AWS

Frontend communicates with the backend via REST APIs.

---

## 📁 Repository Structure

This keeps the system:
	•	Robust
	•	Explainable
	•	Easy to iterate on
