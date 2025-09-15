import pandas as pd

def preprocess_data(df):
    df['category_code'].fillna('unknown.unknown', inplace=True)
    df['brand'].fillna('unknown', inplace=True)
    print("Handled missing values in 'brand' and 'category_code'.")
    
    if pd.api.types.is_datetime64_any_dtype(df['event_time']):
        df['day_of_week'] = df['event_time'].dt.day_name()
        df['hour'] = df['event_time'].dt.hour
        print("Created 'day_of_week' and 'hour' features.")
    
    for col in ['event_type', 'brand', 'day_of_week']:
        if col in df.columns:
            df[col] = df[col].astype('category')
            
    print("Preprocessing complete.")
    return df