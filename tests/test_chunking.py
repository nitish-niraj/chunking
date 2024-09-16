import unittest
from src.chunker import split_into_sections, create_chunks, chunk_structured_document
from src.similarity_checker import load_model

class TestChunking(unittest.TestCase):

    def setUp(self):
        """
        Setup that runs before each test case. Loads the pre-trained model.
        """
        self.model = load_model()
        self.similarity_threshold = 0.7

        # Sample text for testing
        self.sample_text = """1. Introduction
        This is the introduction to the document.
        2. Overview
        This section provides an overview of the document.
        3. Details
        Here are the details of the document."""

        # Expected sections after splitting
        self.expected_sections = [
            "1. Introduction\nThis is the introduction to the document.",
            "2. Overview\nThis section provides an overview of the document.",
            "3. Details\nHere are the details of the document."
        ]

    def test_split_into_sections(self):
        """
        Test if the text is correctly split into sections based on numbered headers.
        """
        sections = split_into_sections(self.sample_text)
        self.assertEqual(sections, self.expected_sections)

    def test_create_chunks(self):
        """
        Test the chunking process to ensure it correctly groups sections based on similarity.
        """
        # Simulate sections
        sections = [
            "This is the first section.",
            "This is the second section which is similar to the first.",
            "This is an entirely different third section."
        ]

        # Chunk the sections using the model
        chunks = create_chunks(sections, self.model, self.similarity_threshold)

        # Verify that the chunking process works (expect 2 chunks: first two similar, last one different)
        self.assertEqual(len(chunks), 2)
        self.assertIn("This is the first section.", chunks[0])
        self.assertIn("This is the second section which is similar to the first.", chunks[0])
        self.assertIn("This is an entirely different third section.", chunks[1])

    def test_chunk_structured_document(self):
        """
        Test the end-to-end chunking process on a structured document.
        """
        # Perform chunking on the sample text
        chunks = chunk_structured_document(self.sample_text, self.similarity_threshold)

        # Verify that the output contains the expected chunks
        self.assertEqual(len(chunks), 3)  # Three separate sections should create three chunks
        self.assertIn("Introduction", chunks[0])
        self.assertIn("Overview", chunks[1])
        self.assertIn("Details", chunks[2])

    def test_chunk_with_empty_text(self):
        """
        Test the chunking process with empty input to ensure graceful handling.
        """
        chunks = chunk_structured_document("", self.similarity_threshold)
        self.assertEqual(chunks, None)

if __name__ == '__main__':
    unittest.main()
