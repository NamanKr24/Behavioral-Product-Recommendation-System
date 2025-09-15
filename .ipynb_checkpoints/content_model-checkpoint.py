import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors # <-- New import

def train_content_based_model(train_df):
    """
    Builds a TF-IDF matrix and fits a NearestNeighbors model.
    """
    product_metadata = train_df[['product_id', 'category_code', 'brand']].drop_duplicates().reset_index(drop=True)
    product_metadata['content'] = product_metadata['category_code'].astype(str) + ' ' + product_metadata['brand'].astype(str)
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(product_metadata['content'])
    nn_model = NearestNeighbors(n_neighbors=11, metric='cosine', algorithm='brute')
    nn_model.fit(tfidf_matrix)
    
    indices = pd.Series(product_metadata.index, index=product_metadata['product_id']).drop_duplicates()
    
    return nn_model, tfidf_matrix, product_metadata, indices

def get_content_recommendations(product_id, nn_model, tfidf_matrix, product_metadata, indices, n=10):
    """
    Generates recommendations for a product using the fitted NearestNeighbors model.
    """
    if product_id not in indices:
        return []
    idx = indices[product_id]
    product_vector = tfidf_matrix[idx]
    distances, neighbor_indices = nn_model.kneighbors(product_vector, n_neighbors=n+1)
    similar_product_indices = neighbor_indices.flatten()[1:]
    
    return product_metadata['product_id'].iloc[similar_product_indices].tolist()