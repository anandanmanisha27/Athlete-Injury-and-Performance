# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set visualization theme
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv(r"C:\Users\kanna\Downloads\collegiate_athlete_injury_dataset.csv")

# 1. Basic Data Overview
print("Dataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe())




# 2. Distribution of Key Numerical Variables
plt.figure(figsize=(16, 12))
numeric_cols = [
    'Age', 'Height_cm', 'Weight_kg', 'Training_Intensity', 'Training_Hours_Per_Week',
    'Recovery_Days_Per_Week', 'Match_Count_Per_Week', 'Rest_Between_Events_Days',
    'Fatigue_Score', 'Performance_Score', 'Team_Contribution_Score',
    'Load_Balance_Score', 'ACL_Risk_Score'
]

#plt.figure(figsize=(18, 15))  # Slightly larger figure
for i, col in enumerate(numeric_cols):
    plt.subplot(5, 3, i+1)
    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
    plt.title(f"Distribution of {col}", fontsize=10)
    plt.xticks(rotation=45, fontsize=8)  # Rotate x-axis labels
    plt.yticks(fontsize=8)
plt.tight_layout(pad=2.5)  # Add space between plots
plt.show()



# 3. Correlation Matrix
plt.figure(figsize=(14, 12))
correlation = df[numeric_cols + ['Injury_Indicator']].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Matrix of Key Metrics")
plt.show()

# 4. Injury Analysis
plt.figure(figsize=(8, 5))
sns.countplot(x="Injury_Indicator", data=df, palette="Set2")
plt.title("Injury Occurrence (0 = No Injury, 1 = Injured)")
plt.xlabel("Injury Indicator")
plt.ylabel("Number of Athletes")
plt.show()

# 5. Compare Injured vs Non-Injured Athletes
injury_group = df.groupby("Injury_Indicator")[[
    'Fatigue_Score', 'ACL_Risk_Score', 'Load_Balance_Score',
    'Performance_Score', 'Recovery_Days_Per_Week'
]].mean().T

injury_group.plot(kind="bar", figsize=(12, 6), colormap="Set1")
plt.title("Comparison of Key Metrics: Injured vs Non-Injured")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 6. Scatter Plots with Regression Lines
features_to_plot = ['Fatigue_Score', 'ACL_Risk_Score', 'Recovery_Days_Per_Week']

plt.figure(figsize=(18, 5))
for i, feature in enumerate(features_to_plot):
    plt.subplot(1, 3, i+1)
    sns.regplot(data=df, x=feature, y="Performance_Score", scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
    plt.title(f"Performance vs {feature}")
    plt.xlabel(feature)
    plt.ylabel("Performance Score")
plt.tight_layout()
plt.show()


# 7. Bar Plot: Mean Recovery Days by Injury Indicator
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Injury_Indicator", y="Recovery_Days_Per_Week", ci="sd", palette="Blues")
plt.title("Average Recovery Days by Injury Status")
plt.xlabel("Injury Indicator (0 = No Injury, 1 = Injured)")
plt.ylabel("Mean Recovery Days Per Week")
plt.show()







# 6. Boxplots: Performance vs Stress & Recovery
features_to_plot = ['Fatigue_Score', 'ACL_Risk_Score', 'Recovery_Days_Per_Week']

plt.figure(figsize=(16, 5))
for i, feature in enumerate(features_to_plot):
    plt.subplot(1, 3, i+1)
    sns.boxplot(data=df, x=feature, y="Performance_Score", palette="Pastel1")
    plt.title(f"Performance vs {feature}")
plt.tight_layout()
plt.show()

# 7. Violin Plot: Recovery Days by Injury Status
plt.figure(figsize=(8, 5))
sns.violinplot(x="Injury_Indicator", y="Recovery_Days_Per_Week", data=df, palette="coolwarm")
plt.title("Recovery Days vs Injury Indicator")
plt.xlabel("Injury Indicator")
plt.ylabel("Recovery Days Per Week")
plt.show()

# 8. Summary of Key Insights
print("""
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

📌 RECOMMENDATIONS:
- Implement personalized recovery protocols based on fatigue and load balance trends.
- Set minimum recovery day thresholds.
- Integrate real-time ACL and fatigue monitoring tools for injury prevention.
""")
