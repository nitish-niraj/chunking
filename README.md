# PDF Chunking Project

This project is designed to chunk large PDF documents into semantically meaningful sections based on sentence similarity using the `sentence-transformers` model. The chunked outputs can be saved as `.txt`, `.json`, or `.csv` formats for further processing or analysis.

## Project Overview

- **Chunking**: This project breaks down a PDF's text into meaningful "chunks" of sentences that are semantically related.
- **Semantic Similarity**: The project uses `sentence-transformers` to calculate the similarity between sentences and groups them based on a threshold.
- **File Handling**: PDF files are read from the `data` directory and chunked outputs are saved in the `output` directory.
- **Output Formats**: The chunked outputs can be saved as `.txt`, `.json`, and `.csv` formats.

## Features

- Extracts text from PDF files using `PyPDF2`.
- Chunks sentences into meaningful sections based on their semantic similarity.
- Allows processing multiple PDF files in batch.
- Outputs the chunked results in `.txt`, `.json`, and `.csv` formats.

## Technologies

- Python 3.x
- Libraries: 
  - `nltk` for sentence tokenization
  - `sentence-transformers` for semantic similarity
  - `scikit-learn` for cosine similarity
  - `PyPDF2` for PDF text extraction
  - `pandas` for saving output in `.csv` format

## Folder Structure

```
pdf_chunking_project/
├── .venv/                     # Virtual environment (optional)
├── data/                      # Input PDF files for processing
├── logs/                      # Log files for chunking process
├── output/                    # Chunked output in txt, json, csv formats
├── src/                       # Source code files for chunking
│   ├── chunker.py             # Main chunking script
│   ├── similarity_checker.py  # Functions for checking semantic similarity
│   ├── utils.py               # Helper functions for saving outputs
├── tests/                     # Test files for unit testing
├── README.md                  # Documentation for the project
├── requirements.txt           # Python dependencies
├── run.py                     # Main script to run the chunking process
```

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/Zenlearn/Chunking-AI-code.git
cd pdf_chunking_project
```

### 2. Set Up Virtual Environment (Optional)
Create a virtual environment to keep dependencies isolated:

```bash
python -m venv .venv
source .venv/Scripts/activate  # For Windows
# or
source .venv/bin/activate      # For macOS/Linux
```

### 3. Install Dependencies
Install all required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Download Required NLTK Data
Ensure NLTK's sentence tokenizer data is downloaded:

```python
python -c "import nltk; nltk.download('punkt')"
```

## How to Run

### 1. Place PDF Files
Place your PDF files into the `data/` directory for processing.

### 2. Run the Chunking Process
Execute the main script to chunk the PDF files:

```bash
python run.py
```

### 3. Check Output
The chunked outputs will be saved in the `output/` directory in `.txt`, `.json`, and `.csv` formats.

## Example Output

Here is an example of chunked output saved as `.txt`:

```
Chunk 1:
This is the first sentence.
This is the second sentence.

Chunk 2:
This is another sentence that forms a meaningful chunk.
```

## Logs
You can check the logs in the `logs/` directory to track the chunking process and any potential errors.

## Tests
Run the unit tests to verify the functionality of the chunking and similarity functions:

```bash
python -m unittest discover tests
```

## Contributing
Feel free to open an issue or submit a pull request if you have any suggestions for improvements.

## License
This project is licensed under the MIT License.