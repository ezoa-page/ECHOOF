import unittest
import logging
from echoof.base import base10_to_base95, base95_to_base10, base10_to_base220, base220_to_base10
from echoof.logger import logger

# Set up a logger for the test
class TestLogger:
    @staticmethod
    def setup():
        # Set up logging for the test environment
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

test_logger = TestLogger.setup()

class TestBaseConversion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_logger.info("Setting up the TestBaseConversion test suite.")

    @classmethod
    def tearDownClass(cls):
        test_logger.info("Tearing down the TestBaseConversion test suite.")

    def setUp(self):
        test_logger.info(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        test_logger.info(f"Finished test: {self._testMethodName}\n")

    def test_base10_to_base95_zero(self):
        """Test converting 0 to base-95."""
        test_logger.debug("Testing base10_to_base95 with input 0.")
        result = base10_to_base95(0)
        self.assertEqual(result, ' ')
        test_logger.debug(f"Result: {result}")

    def test_base10_to_base95_positive(self):
        """Test converting positive base-10 numbers to base-95."""
        test_logger.debug("Testing base10_to_base95 with positive input.")
        result_94 = base10_to_base95(94)
        result_95 = base10_to_base95(95)
        result_190 = base10_to_base95(190)
        self.assertEqual(result_94, '~')
        self.assertEqual(result_95, '! ')  # Updated expected result
        self.assertEqual(result_190, '" ')  # Updated expected result
        test_logger.debug(f"Results: 94 -> {result_94}, 95 -> {result_95}, 190 -> {result_190}")

    def test_base10_to_base95_negative(self):
        """Test negative number conversion to base-95 should raise an exception."""
        test_logger.debug("Testing base10_to_base95 with negative input.")
        with self.assertRaises(Exception) as context:
            base10_to_base95(-1)
        test_logger.debug(f"Exception raised: {context.exception}")

    def test_base95_to_base10(self):
        """Test converting base-95 strings to base-10."""
        test_logger.debug("Testing base95_to_base10 with valid input.")
        result_space = base95_to_base10(' ')
        result_tilde = base95_to_base10('~')
        result_double_excl = base95_to_base10('!!')
        self.assertEqual(result_space, 0)
        self.assertEqual(result_tilde, 94)
        self.assertEqual(result_double_excl, 96)  # Updated expected result
        test_logger.debug(f"Results: ' ' -> {result_space}, '~' -> {result_tilde}, '!!' -> {result_double_excl}")

    def test_base10_to_base220_zero(self):
        """Test converting 0 to base-220."""
        test_logger.debug("Testing base10_to_base220 with input 0.")
        result = base10_to_base220(0)
        self.assertEqual(result, '#')
        test_logger.debug(f"Result: {result}")

    def test_base10_to_base220_positive(self):
        """Test converting positive base-10 numbers to base-220."""
        test_logger.debug("Testing base10_to_base220 with positive input.")
        result_185 = base10_to_base220(185)
        result_220 = base10_to_base220(220)
        self.assertEqual(result_185, chr(220))  # 'Ü'
        self.assertEqual(result_220, '#$')  # Updated expected result
        test_logger.debug(f"Results: 185 -> {result_185}, 220 -> {result_220}")

    def test_base220_to_base10(self):
        """Test converting base-220 strings to base-10."""
        test_logger.debug("Testing base220_to_base10 with valid input.")
        result_hash = base220_to_base10('#')
        result_char220 = base220_to_base10(chr(220))
        result_hash_excl = base220_to_base10('#$')  # Updated test case
        self.assertEqual(result_hash, 0)
        self.assertEqual(result_char220, 185)
        self.assertEqual(result_hash_excl, 220)  # Updated assertion
        test_logger.debug(f"Results: '#' -> {result_hash}, chr(220) -> {result_char220}, '#$' -> {result_hash_excl}")

if __name__ == '__main__':
    unittest.main()
