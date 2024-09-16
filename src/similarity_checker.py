from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logging

def load_model(model_name='sentence-transformers/all-mpnet-base-v2'):
    """
    Load the sentence transformer model.
    Defaults to 'all-mpnet-base-v2' if no model name is provided.
    """
    try:
        logging.info(f"Loading model: {model_name}")
        model = SentenceTransformer(model_name)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        return None

def calculate_similarity(text1, text2, model):
    """
    Calculate the cosine similarity between two pieces of text using a pre-trained model.

    Args:
    - text1: The first piece of text.
    - text2: The second piece of text.
    - model: The pre-loaded SentenceTransformer model.

    Returns:
    - cosine similarity score between 0 and 1.
    """
    try:
        # Encode both pieces of text to get their embeddings
        embeddings = model.encode([text1, text2])

        # Compute cosine similarity between the embeddings
        similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

        logging.info(f"Calculated similarity score: {similarity_score}")
        return similarity_score
    except Exception as e:
        logging.error(f"Error calculating similarity: {e}")
        return None

def is_similar(text1, text2, model, threshold=0.7):
    """
    Determine whether two texts are similar based on a similarity threshold.

    Args:
    - text1: The first piece of text.
    - text2: The second piece of text.
    - model: The pre-loaded SentenceTransformer model.
    - threshold: The similarity threshold (default: 0.7).

    Returns:
    - True if similarity score >= threshold, False otherwise.
    """
    similarity_score = calculate_similarity(text1, text2, model)

    if similarity_score is not None:
        return similarity_score >= threshold
    else:
        return False
