from flask import Flask, request, jsonify
import pandas as pd
import joblib
from model import build_model, get_recommendations
from preprocess import preprocess_data
from database import initialize_client, load_dataset
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model and data
cosine_sim = joblib.load('model.pkl')
 # Ensure you have the dataset saved as a CSV
 
client = initialize_client("AstraCS:THPHfGlAfYkSrRdBBLJOOAWE:7d4f9929a8333acda2525be9b904f339065f8a7d8b62ea65e4b4ba1b85ffee93",
                                   "https://eef27c48-d40e-4643-9629-6c0ac4131b86-us-east-2.apps.astra.datastax.com")

df = load_dataset(client, "books")
df = preprocess_data(df)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    title = data['title']
    recommendations = get_recommendations(title, df, cosine_sim)
    return jsonify(recommendations)


# This should not be in production
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

