import pandas as pd
import glob

# List of file names
file_names = [
    'CSVs/Bot_vs_BENIGN.csv', 'CSVs/DDoS_vs_BENIGN.csv', 'CSVs/DoS GoldenEye_vs_BENIGN.csv',
    'CSVs/DoS Hulk_vs_BENIGN.csv', 'CSVs/DoS Slowhttptest_vs_BENIGN.csv',
    'CSVs/DoS slowloris_vs_BENIGN.csv', 'CSVs/FTP-Patator_vs_BENIGN.csv',
    'CSVs/Heartbleed_vs_BENIGN.csv', 'CSVs/Infiltration_vs_BENIGN.csv',
    'CSVs/PortScan_vs_BENIGN.csv', 'CSVs/SSH-Patator_vs_BENIGN.csv',
    'CSVs/Web Attack – Brute Force_vs_BENIGN.csv',
    'CSVs/Web Attack – Sql Injection_vs_BENIGN.csv', 'CSVs/Web Attack – XSS_vs_BENIGN.csv'
]

# Loop through each file
for file_name in file_names:
    # Read the file using pandas
    data = pd.read_csv(file_name)
    
    # Count the number of benign and attack instances
    num_benign = (data[' Label'] == 'BENIGN').sum()
    num_attack = (data[' Label'] != 'BENIGN').sum()
    
    # Print information
    print(f"File: {file_name}")
    print(f"Number of Benign instances: {num_benign}")
    print(f"Number of Attack instances: {num_attack}")
    print("Shape of the dataset:", data.shape)
    print("-----------------------------")