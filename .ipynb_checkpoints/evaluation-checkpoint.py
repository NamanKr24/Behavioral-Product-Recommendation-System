def precision_at_k(k, recommended_items, actual_items):
    if not recommended_items:
        return 0.0
    top_k_recs = recommended_items[:k]
    
    hits = len(set(top_k_recs) & set(actual_items))
    
    return hits / k

def recall_at_k(k, recommended_items, actual_items):
    if not actual_items:
        return 0.0
    
    top_k_recs = recommended_items[:k]
    
    hits = len(set(top_k_recs) & set(actual_items))
    
    return hits / len(actual_items)