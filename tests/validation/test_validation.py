import unittest
from src.validation import validation


class TestValidation(unittest.TestCase):

    def test_validates_proper_header(self):
        self.assertTrue(validation.is_valid_header('Content-Length: 303'))

    def test_invalidates_improper_header(self):
        self.assertFalse(validation.is_valid_header('Improper'))
