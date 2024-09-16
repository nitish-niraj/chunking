import os
import json
import csv
import logging

def save_chunks_as_txt(chunks, output_path):
    """
    Save the chunks of text into a .txt file.

    Args:
    - chunks: List of chunked text.
    - output_path: Path where the .txt file will be saved.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for i, chunk in enumerate(chunks, 1):
                file.write(f"Chunk {i}:\n{chunk}\n{'='*50}\n")
        logging.info(f"Chunks saved as .txt file at {output_path}")
    except Exception as e:
        logging.error(f"Error saving chunks as .txt file: {e}")

def save_chunks_as_json(chunks, output_path):
    """
    Save the chunks of text into a .json file.

    Args:
    - chunks: List of chunked text.
    - output_path: Path where the .json file will be saved.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump({'chunks': chunks}, file, ensure_ascii=False, indent=4)
        logging.info(f"Chunks saved as .json file at {output_path}")
    except Exception as e:
        logging.error(f"Error saving chunks as .json file: {e}")

def save_chunks_as_csv(chunks, output_path):
    """
    Save the chunks of text into a .csv file.

    Args:
    - chunks: List of chunked text.
    - output_path: Path where the .csv file will be saved.
    """
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Chunk Number', 'Chunk Text'])
            for i, chunk in enumerate(chunks, 1):
                writer.writerow([i, chunk])
        logging.info(f"Chunks saved as .csv file at {output_path}")
    except Exception as e:
        logging.error(f"Error saving chunks as .csv file: {e}")

def ensure_directory_exists(directory_path):
    """
    Ensure that the specified directory exists. If not, create it.

    Args:
    - directory_path: Path of the directory to ensure.
    """
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            logging.info(f"Directory {directory_path} created.")
        except Exception as e:
            logging.error(f"Error creating directory {directory_path}: {e}")
    else:
        logging.info(f"Directory {directory_path} already exists.")
