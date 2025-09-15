import pandas as pd
from surprise import Reader, Dataset, SVD

def train_collaborative_model(train_df):
    event_weights = {'view': 1.0, 'cart': 2.0, 'purchase': 4.0}
    train_df['rating'] = train_df['event_type'].map(event_weights).fillna(0)
    
    ratings_df = train_df[['user_id', 'product_id', 'rating']]
    reader = Reader(rating_scale=(0, 4))
    data = Dataset.load_from_df(ratings_df, reader)
    trainset = data.build_full_trainset()
    
    algo = SVD(n_epochs = 10, verbose = True)
    algo.fit(trainset)
    return algo

def get_collaborative_recommendations(user_id, all_product_ids, interacted_items, algo, n=10):
    predictions = [algo.predict(user_id, pid) for pid in all_product_ids if pid not in interacted_items]
    predictions.sort(key=lambda x: x.est, reverse=True)
    top_n_recs = [pred.iid for pred in predictions[:n]]
    return top_n_recs