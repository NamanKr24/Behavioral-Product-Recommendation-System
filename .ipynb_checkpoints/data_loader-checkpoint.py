import pandas as pd

def load_cosmetics_data():
    file_path = './2019-Oct.csv'
    df = pd.read_csv(file_path)
    sample_size = int(len(df)*0.25)
    df = df.head(sample_size)
    print(f"Successfully loaded {file_path}")
    return df