from flask import Flask, jsonify
import pickle

app = Flask(__name__)
try:
    with open('svd_model.pkl', 'rb') as f:
        algo = pickle.load(f)
    with open('all_product_ids.pkl', 'rb') as f:
        all_product_ids = pickle.load(f)
    print("Model and artifacts loaded successfully.")
except FileNotFoundError:
    print("Error: Make sure 'svd_model.pkl' and 'all_product_ids.pkl' are present.")
    algo = None
    all_product_ids = []

@app.route('/recommend/<int:user_id>')
def get_recommendations(user_id):
    """
    Takes a user_id from the URL and returns product recommendations.
    """
    if algo is None:
        return jsonify({"error": "Model not loaded"}), 500

    print(f"Generating recommendations for User ID: {user_id}")
    
    predictions = [algo.predict(uid=user_id, iid=pid) for pid in all_product_ids]
    
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    top_10_recs = [pred.iid for pred in predictions[:10]]
    
    return jsonify({
        "user_id": user_id,
        "recommendations": top_10_recs
    })

if __name__ == '__main__':
    app.run(debug=True)