
import pandas as pd

def load_data(data_path):
    
    # Import the data from 'credit.csv'
    df = pd.read_csv(data_path)
    
    
    try:
        # Import the data from csv file
        df = pd.read_csv(data_path)

        return df

    except FileNotFoundError:
        print(f"Error: File not found at {data_path}. Please check the file path.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None



