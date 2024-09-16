import unittest
from src.similarity_checker import load_model, calculate_similarity, is_similar

class TestSimilarityChecker(unittest.TestCase):

    def setUp(self):
        """
        Setup that runs before each test case.
        Loads the pre-trained model.
        """
        self.model = load_model()
        self.similarity_threshold = 0.7

        # Sample text sections for testing
        self.text1 = "This is the first section of the document."
        self.text2 = "This is another section of the document which is slightly different."
        self.text3 = "This is completely unrelated content with no similarity."

    def test_model_loading(self):
        """
        Test if the model is loaded successfully.
        """
        self.assertIsNotNone(self.model, "Model failed to load.")

    def test_calculate_similarity(self):
        """
        Test if the cosine similarity between two similar sections is computed correctly.
        """
        similarity_score = calculate_similarity(self.text1, self.text2, self.model)
        self.assertIsInstance(similarity_score, float, "Similarity score should be a float.")
        self.assertGreaterEqual(similarity_score, 0, "Similarity score should be between 0 and 1.")
        self.assertLessEqual(similarity_score, 1, "Similarity score should be between 0 and 1.")

    def test_is_similar_above_threshold(self):
        """
        Test if is_similar() correctly returns True for similar sections based on the threshold.
        """
        # Using two texts that are similar
        result = is_similar(self.text1, self.text2, self.model, self.similarity_threshold)
        self.assertTrue(result, "Expected True for similar texts based on the threshold.")

    def test_is_similar_below_threshold(self):
        """
        Test if is_similar() correctly returns False for dissimilar sections based on the threshold.
        """
        # Using two texts that are dissimilar
        result = is_similar(self.text1, self.text3, self.model, self.similarity_threshold)
        self.assertFalse(result, "Expected False for dissimilar texts based on the threshold.")

    def test_is_similar_with_different_threshold(self):
        """
        Test if is_similar() behaves correctly with a different threshold.
        """
        # Use a very low threshold to ensure the sections pass the similarity check
        low_threshold = 0.1
        result = is_similar(self.text1, self.text3, self.model, low_threshold)
        self.assertTrue(result, "Expected True when the threshold is very low.")

if __name__ == '__main__':
    unittest.main()
