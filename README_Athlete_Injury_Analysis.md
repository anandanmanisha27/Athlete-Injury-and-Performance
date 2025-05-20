# Collegiate Athlete Injury Risk Analysis

This project analyzes a dataset of collegiate athletes to explore patterns and risk factors associated with sports injuries. It includes data visualization, correlation analysis, and statistical insights into the role of fatigue, recovery, and performance metrics.

---

## 📊 Dataset Overview

- **File Name**: `collegiate_athlete_injury_dataset.csv`
- **Target Variable**: `Injury_Indicator` (0 = No Injury, 1 = Injured)
- **Features Analyzed**:
  - Demographics: Age, Height, Weight
  - Training: Training Intensity, Training Hours Per Week, Match Count
  - Recovery: Recovery Days Per Week, Rest Between Events
  - Health Metrics: Fatigue Score, ACL Risk Score, Load Balance Score
  - Performance Metrics: Performance Score, Team Contribution Score

---

## 🔍 Project Objectives

- Understand the distribution of physical and training attributes.
- Identify key factors associated with injury risk.
- Visualize correlations between fatigue, recovery, performance, and injury occurrence.
- Generate actionable insights to reduce injury rates.

---

## 📈 Analysis Summary

### 1. **Descriptive Analysis**
- Dataset shape and basic statistics
- Missing values overview

### 2. **Visualizations**
- Histograms of all numerical features
- Correlation matrix of all key metrics and injury status
- Bar charts comparing injured vs. non-injured athletes
- Regression plots showing impact on performance
- Average recovery days comparison by injury group

### 3. **Key Insights**

```
🔍 KEY INSIGHTS:

1. Athletes with higher fatigue and ACL risk scores are significantly more likely to be injured.
2. Recovery days per week are lower on average among injured athletes, indicating recovery as a key protective factor.
3. Performance scores are negatively impacted by high fatigue and ACL risk.
4. Load balance score is positively correlated with performance and negatively with injury risk.
5. The strongest correlations with injury were found in:
   - ACL Risk Score (+0.68)
   - Fatigue Score (+0.55)
   - Recovery Days (-0.42)
6. Athletes with fewer than 2 recovery days per week showed a sharp increase in injury prevalence.
```

---

## 📦 Dependencies

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

---

## ▶️ How to Run

1. Ensure the dataset is available at the specified path.
2. Run each cell in the Jupyter notebook in sequence.
3. Review plots and printed insights for findings.
4. Modify code to explore other features or groups of interest.

---

## 🚀 Future Enhancements

- Integrate predictive modeling (e.g., logistic regression, XGBoost) for injury prediction.
- Explore time-series tracking or player-level injury progression.
- Develop a real-time Digital Twin model for athlete monitoring and alerts.

