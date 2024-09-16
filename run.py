import os
import logging
from src.chunker import chunk_structured_document
from src.utils import save_chunks_as_txt, save_chunks_as_json, save_chunks_as_csv
from PyPDF2 import PdfReader

# Set up logging
logging.basicConfig(
    filename='logs/chunking.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyPDF2.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
            return text
    except Exception as e:
        logging.error(f"Failed to extract text from {file_path}: {e}")
        return None

def process_pdfs(input_dir, output_dir):
    """
    Process all PDF files in the input directory and save the chunked output to the output directory.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all PDF files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_dir, filename)
            logging.info(f"Processing {filename}")

            # Extract text from PDF
            pdf_content = extract_text_from_pdf(file_path)
            if not pdf_content:
                logging.error(f"Skipping {filename} due to extraction failure.")
                continue

            # Chunk the text using semantic similarity
            chunks = chunk_structured_document(pdf_content)
            if not chunks:
                logging.error(f"No chunks created for {filename}.")
                continue

            # Save the chunks in different formats
            base_filename = os.path.splitext(filename)[0]  # Filename without extension
            txt_output_path = os.path.join(output_dir, f"{base_filename}_chunked.txt")
            json_output_path = os.path.join(output_dir, f"{base_filename}_chunked.json")
            csv_output_path = os.path.join(output_dir, f"{base_filename}_chunked.csv")

            save_chunks_as_txt(chunks, txt_output_path)
            save_chunks_as_json(chunks, json_output_path)
            save_chunks_as_csv(chunks, csv_output_path)

            logging.info(f"Chunking and saving completed for {filename}")

if __name__ == "__main__":
    input_dir = 'data'        # Directory containing the PDF files
    output_dir = 'output'     # Directory where the chunked output will be saved

    logging.info("Starting PDF chunking process.")
    process_pdfs(input_dir, output_dir)
    logging.info("PDF chunking process completed.")

