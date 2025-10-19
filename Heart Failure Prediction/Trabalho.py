import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Lendo o dataset
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    
    print(df.head())
    
    

if __name__ == "__main__":
    main()