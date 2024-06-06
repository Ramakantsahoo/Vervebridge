# model.py
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

def build_model(df):
    try:
        logger.info("Building recommendation model")
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return cosine_sim
    except Exception as e:
        logger.error("Error building recommendation model: %s", e)
        raise

# Function to get book recommendations
def get_recommendations(title, df, model):
    if title not in df['Title'].values:
        return []  

    idx = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(model[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:]  

    # Collect unique book indices
    unique_book_indices = []
    seen_titles = set()
    for i, score in sim_scores:
        if len(unique_book_indices) == 10:
            break
        book_title = df['Title'].iloc[i]
        if book_title != title and book_title not in seen_titles:
            unique_book_indices.append(i)
            seen_titles.add(book_title)

    # Return the top 10 most similar book titles as a list
    return df['Title'].iloc[unique_book_indices].tolist()

