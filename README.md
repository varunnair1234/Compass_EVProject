# ⚡ Compass: EVProject

Compass is an intelligent web application designed to simplify the transition to electric mobility. By combining real-time data tracking with neural-network-driven insights, Compass helps users manage battery health, locate optimized charging, and find the perfect vehicle.

## 👥 Project Team

| Team Member | Role | Location | Time Zone |
| :--- | :--- | :--- | :--- |
| **Varun Nair** | Engineer | Santa Cruz, CA | PST |
| **Nisheeth Chowdary Velicheti** | Engineer | Santa Cruz, CA | PST |
| **Venkata Sai Anand Yadlapati** | Engineer | Santa Cruz, CA | PST |

---

## ✨ Features

### 🔋 Battery Tracker
* **Monitoring:** Track odometer, full-charge range, and State-of-Health (SoH).
* **Predictive ML:** Estimate battery degradation trends and predict near-term health using baseline models.

### ⚡ Charge Finder
* **Live Search:** Locate nearby charging stations via NREL API.
* **Ranking Engine:** Stations are ranked based on distance, power compatibility, and reliability.

### 🚗 Neural Recommendation (New)
* **Neural Calibration:** A PyTorch-based model that automatically predicts user priorities (Price vs. Range) based on income and commute metrics.
* **Weighted Scoring:** Transparent vehicle ranking using Min-Max scaling to match users with the best 130+ verified EV models.

---

## 🏗️ Architecture & ML Pipeline

Compass is built with a "ML-First" philosophy, moving from data ingestion to production-ready neural networks.

1. **Data Engineering (`01_data_processing`):** Cleaned 3,400+ raw records, standardized units, and handled multi-currency pricing anomalies.
2. **Neural Training (`03_neural_calibration`):** Built a PyTorch Feedforward Neural Network using **Softmax Activation** to calibrate user preferences.
3. **Model Export (`04_model_export`):** Intelligence is exported as `.pth` artifacts, allowing the FastAPI backend to load the "brain" without retraining.

* **Frontend:** Static HTML/CSS/JS (`index.html`)
* **Backend:** FastAPI (Python)
* **ML Framework:** PyTorch
* **Infrastructure:** AWS

---

## 📁 Repository Structure

* `notebooks/`: End-to-end ML lifecycle (Processing, Simulation, Training, Export).
* `data/`: Raw and high-integrity cleaned EV datasets.
* `saved_models/`: Production-ready PyTorch model binaries.
* `compiled_vehicle_models_data.csv`: Source data.