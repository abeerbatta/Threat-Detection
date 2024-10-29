# Importing the libraries
import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import resample
from sklearn import preprocessing
from warnings import simplefilter
from imblearn.under_sampling import RandomUnderSampler

# Suppress FutureWarning messages
simplefilter(action='ignore', category=FutureWarning)

# Record start time
start_time = time.time()

# Load the main dataset (all_data.csv)
main_dataset = pd.read_csv("CSVs/combined_data.csv")

# List of attack types and BENIGN
attack_types = ["Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris", "FTP-Patator",
                "Heartbleed", "Infiltration", "PortScan", "SSH-Patator", "Web Attack – Brute Force",
                "Web Attack – Sql Injection", "Web Attack – XSS"]
benign_type = "BENIGN"

# Loop through each attack type
for attack_type in attack_types:
    # Create a DataFrame for the current attack type
    attack_data = main_dataset[main_dataset[" Label"] == attack_type]
    
    # Create a DataFrame for BENIGN data
    benign_data = main_dataset[main_dataset[" Label"] == benign_type]
    
    # Concatenate the attack and benign data
    combined_data = pd.concat([attack_data, benign_data], axis=0)
    
    # Shuffle the combined data
    combined_data = combined_data.sample(frac=1, random_state=42)
    
    # Save the combined data to a CSV file
    output_filename = f"{attack_type}_vs_{benign_type}.csv"
    combined_data.to_csv(output_filename, index=False)
    print(f"Saved {output_filename}")

# Calculate and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")