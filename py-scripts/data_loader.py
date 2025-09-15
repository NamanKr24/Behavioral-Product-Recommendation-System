import pandas as pd
import glob

def load_kaggle_data_all_months():
    path = '/kaggle/input/ecommerce-events-history-in-cosmetics-shop'
    all_csv_files = glob.glob(f'{path}/*.csv')
    
    df_list = [pd.read_csv(file) for file in all_csv_files]
    full_df = pd.concat(df_list, ignore_index=True)
    
    return full_df