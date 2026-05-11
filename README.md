# 🛢️ MWD Drilling Optimization using Machine Learning

## 📌 Problem Statement
Drilling operations in oil & gas are highly sensitive to inefficiencies, which directly increase operational cost and non-productive time (NPT). Optimizing drilling performance, particularly Rate of Penetration (ROP), is critical for improving operational efficiency.

---

## 🎯 Objective
To develop a machine learning model that predicts drilling performance (ROP) using MWD/LWD-derived drilling parameters and identifies key factors affecting drilling efficiency.

---

## 📊 Dataset
This project uses a **simulated MWD dataset** designed based on real-world drilling engineering principles and parameter relationships.

The dataset includes realistic interactions between drilling variables such as:

- Depth (m)  
- Weight on Bit (WOB)  
- RPM  
- Flow Rate  
- Mud Weight  
- Inclination  
- Torque  
- Standpipe Pressure  
- ROP (target variable)

Due to data confidentiality constraints, no proprietary or field data is used. Instead, the dataset reflects realistic drilling behavior trends observed in oil & gas operations.

---

## ⚙️ Methodology

1. Data generation / simulation based on drilling engineering relationships  
2. Data preprocessing and feature engineering  
3. Exploratory Data Analysis (EDA)  
4. Machine Learning model development for ROP prediction  
5. Model evaluation and interpretation  

---

## 🛠 Tech Stack

- Python (Pandas, NumPy, Scikit-learn) – data processing and machine learning  
- SQL (MySQL / PostgreSQL) – structured data handling and storage  
- Streamlit – interactive web dashboard for model visualization  
- Matplotlib / Seaborn – data analysis and visualization  
- Git & GitHub – version control and project management  

---

## Results

Multiple machine learning models were evaluated for predicting Rate of Penetration (ROP) using simulated MWD drilling parameters.

Linear Regression achieved the strongest performance:

- MAE: 3.33
- R² Score: 0.87

More complex ensemble methods such as Random Forest and XGBoost underperformed on the simulated dataset, suggesting predominantly linear relationships between drilling parameters and ROP.

Feature importance analysis identified RPM, Depth, and WOB as the primary drivers influencing drilling performance.

### Model Comparison Table

| Model             | MAE  | R²   |
| ----------------- | ---- | ---- |
| Linear Regression | 3.33 | 0.87 |
| Random Forest     | 4.24 | 0.79 |
| XGBoost           | 4.61 | 0.76 |


---

## Engineering Interpretation

The results indicate that drilling performance within the simulated environment follows relatively structured and near-linear behavior patterns. While advanced ensemble models were evaluated, simpler linear models generalized more effectively.

This highlights the importance of matching machine learning model complexity to drilling data characteristics rather than assuming more complex algorithms will always perform better.

---

## 💡 Operational Relevance

This project demonstrates how machine learning can be applied in oil & gas drilling operations to:

- Improve drilling efficiency  
- Reduce non-productive time (NPT)  
- Support data-driven decision-making in drilling operations  
- Bridge petroleum engineering domain knowledge with modern data science techniques  

---

## 🧠 Domain Insight

This work is grounded in petroleum engineering principles, particularly drilling mechanics and MWD/LWD data interpretation, combined with machine learning techniques for predictive analytics.
