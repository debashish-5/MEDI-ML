# Health Supplement Data Analysis & Machine Learning Project

## Overview
This project focuses on **data collection, analysis, visualization, and machine learning** for **health supplement, medicine, skincare, and body lotion products**.  
It includes **data collection, preprocessing, visualization, and predictive modeling** — all integrated into a complete data science workflow.

---

## Project Structure

| File / Folder | Description |
|----------------|-------------|
| **1_protein.ipynb** | Data collection and preprocessing for protein supplement products. |
| **2_medicine.ipynb** | Data analysis and cleaning of medicine-related product data. |
| **3_skincare.ipynb** | Data exploration and visualization for skincare products. |
| **4_bodylotion.ipynb** | Analysis of body lotion product dataset. |
| **5_Data Analysis.ipynb** | Combined analysis across all product datasets for comparative insights. |
| **6_Visualization.ipynb** | Advanced visualizations and dashboards for better understanding of product trends. |
| **7_ML.ipynb** / **FINAL_ML.ipynb** | Machine learning models for predicting product ratings, pricing, or demand. |
| **flask-2.py** | Flask backend for integrating ML model into a web app. |
| **visualize.pbix** | Power BI dashboard showing key business insights. |
| **Screenshot.png / Visualization -BI.png** | Preview images of visualizations and dashboards. |
| **test.csv** | Sample test dataset for ML model evaluation. |
| **model.pkl** | Joblib File. |
| **pipeline.pkl** | Pipeline File. |
| **1_health_supplement.csv**, **2_health_supplement.csv**, **3_health_supplement.csv**, **4_health_supplement.csv**, **5_total_health_supplement.csv**, **final_health_supplement.csv** | CSV datasets used across stages of the project. |

---

## Features
- **Web Scraping & Data Cleaning** – Extracted and processed product data from multiple sources.
- **Exploratory Data Analysis (EDA)** – Identified key insights like price trends, rating distributions, and brand performance.
- **Data Visualization** – Created clear visual insights using Matplotlib, Seaborn, and Power BI.
- **Machine Learning** – Built predictive models to estimate ratings, pricing, or product popularity.
- **Flask Integration** – Developed a simple Flask app for deploying the ML model.

---

## Tech Stack
- **Languages:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Tools:** Jupyter Notebook, Power BI, Flask  
- **Version Control:** Git & GitHub  

---

## Machine Learning Workflow
1. **Data Preprocessing** – Cleaned missing values, handled duplicates, and standardized features.  
2. **Feature Engineering** – Extracted meaningful columns such as price, rating, and brand.  
3. **Model Building** – Trained ML models (e.g., Linear Regression, Decision Tree, Random Forest).  
4. **Evaluation** – Measured performance using metrics like R², MSE, and accuracy.  
5. **Deployment** – Exported the model for integration with Flask-based web interface.

---

## Insights
- Found correlation between product price and customer rating.
- Discovered brand-specific performance variations.
- Built models capable of predicting approximate product performance metrics.

---

## Power BI Dashboard
The Power BI file (`visualize.pbix`) provides:
- Category-wise sales and rating analysis  
- Brand distribution visualizations  
- Trend comparisons across product types  

---

## How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/debashish-5.git
cd debashish-5
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run Jupyter Notebooks
```bash
Open each .ipynb file in Jupyter Notebook or VS Code to explore data analysis steps.
```
### 4️⃣ Run Flask App
```bash
python flask-2.py
```
## Author
### Debashish Parida
