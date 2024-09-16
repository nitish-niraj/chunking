import nltk
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logging

nltk.download('punkt')

def split_into_sentences(text):
    """
    Split the input text into sentences using NLTK's sentence tokenizer.
    """
    sentences = sent_tokenize(text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def create_meaningful_chunks(sentences, model, similarity_threshold=0.75):
    """
    Group sentences into meaningful chunks based on semantic similarity.
    
    Args:
    - sentences: List of individual sentences.
    - model: Pre-trained sentence transformer model.
    - similarity_threshold: Threshold for cosine similarity to group sentences.

    Returns:
    - List of chunks where each chunk is a group of related sentences.
    """
    chunks = []
    current_chunk = []

    for sentence in sentences:
        # If there is no chunk or the sentence is not similar to the current chunk, create a new chunk
        if not current_chunk or not is_similar(current_chunk, sentence, model, similarity_threshold):
            if current_chunk:
                chunks.append(' '.join(current_chunk))  # Add the current chunk as a group of sentences
            current_chunk = [sentence]  # Start a new chunk with the current sentence
        else:
            current_chunk.append(sentence)  # If similar, add the sentence to the current chunk

    # Append the last chunk if it exists
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def is_similar(chunk, sentence, model, threshold=0.75):
    """
    Check if the given sentence is semantically similar to the current chunk using cosine similarity.

    Args:
    - chunk: Current list of sentences in the chunk.
    - sentence: A new sentence to compare against the chunk.
    - model: Pre-trained sentence transformer model.
    - threshold: Cosine similarity threshold for considering the sentence as related.

    Returns:
    - True if the sentence is similar to the chunk, False otherwise.
    """
    chunk_text = ' '.join(chunk)  # Join the chunk into a single string for comparison
    embeddings = model.encode([chunk_text, sentence])  # Encode the chunk and the sentence
    similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]  # Calculate similarity

    logging.info(f"Similarity score between chunk and sentence: {similarity_score}")
    
    return similarity_score >= threshold  # Return True if similarity is above the threshold

def chunk_structured_document(content, similarity_threshold=0.75):
    """
    Main function to chunk a document into meaningful groups of sentences based on semantic similarity.

    Args:
    - content: Full document text.
    - similarity_threshold: Threshold for semantic similarity.

    Returns:
    - List of chunks (grouped sentences).
    """
    try:
        # Load the pre-trained sentence transformer model
        model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

        # Step 1: Split the document into individual sentences
        sentences = split_into_sentences(content)
        logging.info(f"Document split into {len(sentences)} sentences.")

        # Step 2: Group sentences into meaningful chunks
        chunks = create_meaningful_chunks(sentences, model, similarity_threshold)
        logging.info(f"{len(chunks)} chunks created.")

        return chunks
    except Exception as e:
        logging.error(f"Error in chunk_structured_document: {e}")
        return None
