import re
import logging
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyPDF2.

    Args:
    - file_path: Path to the PDF file.

    Returns:
    - Extracted text from the PDF file.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
            logging.info(f"Text extracted successfully from {file_path}")
            return text
    except Exception as e:
        logging.error(f"Failed to extract text from {file_path}: {e}")
        return None

def split_into_sections(text):
    """
    Split the input text into sections based on numbered headers (e.g., "1. Introduction").

    Args:
    - text: Full text extracted from the PDF.

    Returns:
    - A list of text sections.
    """
    # Split text using regex to capture numbered sections like '1. ', '2. ', etc.
    try:
        sections = re.split(r'\n(?=\d+\.\s)', text)
        logging.info(f"Document split into {len(sections)} sections.")
        return [section.strip() for section in sections if section.strip()]
    except Exception as e:
        logging.error(f"Error splitting text into sections: {e}")
        return []

def clean_text(text):
    """
    Clean the extracted text (optional step, depends on your needs).

    Args:
    - text: Raw text extracted from the PDF.

    Returns:
    - Cleaned text, with unnecessary characters or line breaks removed.
    """
    # Example: Remove multiple newlines and extra spaces
    try:
        cleaned_text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single newline
        cleaned_text = cleaned_text.strip()
        logging.info("Text cleaned successfully.")
        return cleaned_text
    except Exception as e:
        logging.error(f"Error cleaning text: {e}")
        return text
