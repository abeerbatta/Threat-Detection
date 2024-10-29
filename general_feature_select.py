import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import os

combined_data = pd.read_csv("CSVs/combined_data.csv")
def perform_feature_selection(data):
    X = data.drop(columns=[" Label"])
    y = data[" Label"].apply(lambda x: 1 if x != "BENIGN" else 0)
    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    clf.fit(X, y)
    
    feature_importances = clf.feature_importances_
    return feature_importances
# Perform feature selection on the combined_data file
importance_list = perform_feature_selection(combined_data)

# Create a DataFrame for importance list
importance_df = pd.DataFrame({"Feature": combined_data.drop(columns=[" Label"]).columns,
                              "Importance": importance_list})

# Calculate the percentage of importance for each feature
total_importance = importance_df["Importance"].sum()
importance_df["Percentage"] = importance_df["Importance"] / total_importance * 100

# Sort the DataFrame by importance in descending order
importance_df = importance_df.sort_values(by="Importance", ascending=False)

# Print the top 20 features and their percentages
print("\nTop 20 features and their percentages for combined_data:")
print(importance_df.head(20))

# Save the importance list to a CSV file
importance_filename = "combined_data_importance.csv"
importance_df.to_csv(importance_filename, index=False)
print("Saved importance list for combined_data")

# Create a bar plot for the top 20 features' importances
plt.figure(figsize=(10, 6))
top_20_df = importance_df.head(20)
top_20_df.plot(kind="bar", x="Feature", y="Importance", legend=None)
plt.title("Feature Importance for combined_data")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()