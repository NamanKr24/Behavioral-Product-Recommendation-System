import pandas as pd

def get_baseline_recommendations(train_df, n=10):
    popular_recs = train_df[train_df['event_type'] == 'purchase']['product_id'].value_counts().head(n).index.tolist()
    return popular_recs