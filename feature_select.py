import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
import os

# List of attack types and BENIGN
#
attack_types = [ "Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", 
                "DoS Slowhttptest", "DoS slowloris", "FTP-Patator", "Heartbleed", "Infiltration", 
                "PortScan", "SSH-Patator", 
                "Web Attack - Brute Force", "Web Attack - Sql Injection",
                 "Web Attack - XSS"]
benign_type = "BENIGN"

# Function for feature selection and importance list creation
def perform_feature_selection(data):
    print(f"Processing dataset with shape: {data.shape}")
    
    label_column = ' Label'  # We now know the exact column name
    
    X = data.drop(columns=[label_column])
    y = data[label_column].apply(lambda x: 1 if x != benign_type else 0)
    
    print("Training RandomForest...")
    clf = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)
    clf.fit(X, y)
    
    print("Feature selection complete!")
    return clf.feature_importances_

# Iterate over attack types
for i, attack_type in enumerate(attack_types, 1):
    print(f"\nProcessing attack type {i}/{len(attack_types)}: {attack_type}")
    
    # Load the attack vs. benign file
    input_filename = f"CSVs/{attack_type}_vs_{benign_type}.csv"
    print(f"Loading {input_filename}...")
    attack_data = pd.read_csv(input_filename, low_memory=False)
    
    # Perform feature selection
    importances = perform_feature_selection(attack_data)
    
    # Create a DataFrame for importance list
    importance_df = pd.DataFrame({
        "Feature": attack_data.drop(columns=[' Label']).columns,
        "Importance": importances
    })
    
    # Calculate the percentage of importance for each feature
    total_importance = importance_df["Importance"].sum()
    importance_df["Percentage"] = importance_df["Importance"] / total_importance * 100
    
    # Sort the DataFrame by importance in descending order
    importance_df = importance_df.sort_values(by="Importance", ascending=False)
    
    # Print the top 20 features and their percentages
    print(f"\nTop 20 features and their percentages for {attack_type}:")
    print(importance_df.head(20))
    
    # Save the importance list to a CSV file
    importance_filename = f"{attack_type}_importance.csv"
    importance_df.to_csv(importance_filename, index=False)
    print(f"Saved importance list to {importance_filename}")
    
    # Create a bar plot for the top 20 features' importances
    plt.figure(figsize=(15, 8))
    top_20_df = importance_df.head(20)
    plt.bar(range(len(top_20_df)), top_20_df["Importance"])
    plt.xticks(range(len(top_20_df)), top_20_df["Feature"], rotation=45, ha='right')
    plt.title(f"Top 20 Feature Importance for {attack_type}")
    plt.xlabel("Feature")
    plt.ylabel("Importance")
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(f"{attack_type}_importance.png")
    print(f"Saved plot to {attack_type}_importance.png")
    plt.close()

print("\nFeature selection and visualization completed for all attack types!")