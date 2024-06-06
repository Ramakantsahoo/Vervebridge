import logging
from logging_config import setup_logging
from database import initialize_client, load_dataset
from eda import explore_dataset, plot_distributions
from preprocess import preprocess_data
from model import build_model, get_recommendations
import joblib

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting the Book Recommendation System")

    try:
        # Initialize the client and load the dataset
        client = initialize_client("AstraCS:THPHfGlAfYkSrRdBBLJOOAWE:7d4f9929a8333acda2525be9b904f339065f8a7d8b62ea65e4b4ba1b85ffee93",
                                   "https://eef27c48-d40e-4643-9629-6c0ac4131b86-us-east-2.apps.astra.datastax.com")
        df = load_dataset(client, "books")

        # Explore the dataset
        explore_dataset(df)
        plot_distributions(df)

        # Preprocess the data
        df = preprocess_data(df)

        # Build the recommendation model
        cosine_sim = build_model(df)
        joblib.dump(cosine_sim, 'model.pkl')
        print("Model saved successfully!")

        # Test the recommendation system
        # recommendations = get_recommendations('Grapes of Wrath, The', df, cosine_sim)
        print("Recommendations for 'Grapes of Wrath, The': ", get_recommendations('Grapes of Wrath, The', df, cosine_sim))
    except Exception as e:
        logger.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
