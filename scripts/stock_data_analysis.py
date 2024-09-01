import pandas as pd
import matplotlib.pyplot as plt
import talib
import pynance as pn
import glob
import os

class stockeda:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def load_data(self):
        # Load all CSV files
        all_files = glob.glob(os.path.join(self.folder_path, "*.csv"))
        
        # Init an empty list to hold dataframes
        df_list = []
        
        for file in all_files:
            # Extract the stock symbol from the file name
            filename = os.path.basename(file)
            stock_symbol = filename.split('_')[0]
            df = pd.read_csv(file) # Read the CSV file into a dataframe
            df['stock_symbol'] = stock_symbol  # Add the stock_symbol column to the dataframe
            df_list.append(df) # Append the dataframe to the list
   
        self.data = pd.concat(df_list, ignore_index=True)   # Concatenate all dataframes
        self.data['Date'] = pd.to_datetime(self.data['Date']) # Convert the 'Date' column to datetime
        
        return self.data  # return the expected data
