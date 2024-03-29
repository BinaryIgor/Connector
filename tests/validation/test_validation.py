import unittest
from src.validation import validation


class TestValidation(unittest.TestCase):

    def test_validates_proper_header(self):
        self.assertTrue(validation.is_valid_header('Content-Length: 303'))

    def test_invalidates_improper_header(self):
        self.assertFalse(validation.is_valid_header('Improper'))

    def test_validates_proper_ip(self):
        self.assertTrue(validation.is_valid_ip('192.168.0.122'))

    def test_invalidates_improper_ip_case1(self):
        self.assertFalse(validation.is_valid_ip('192.168.2'))

    def test_invalidates_improper_ip_case2(self):
        self.assertFalse(validation.is_valid_ip('Ala.bala.defg.zv'))

    def test_invalidates_improper_ip_case3(self):
        self.assertFalse(validation.is_valid_ip('192.ala.'))

    def test_validates_proper_port(self):
        self.assertTrue(validation.is_valid_port(4000))

    def test_invalidates_improper_port_case1(self):
        self.assertFalse(validation.is_valid_port(validation.MIN_PORT - 1))

    def test_invalidates_improper_port_case2(self):
        self.assertFalse(validation.is_valid_port(validation.MAX_PORT + 1))

    def test_validates_positive_number_case1(self):
        self.assertTrue(validation.is_positive_number(22))

    def test_validates_positive_number_case2(self):
        self.assertTrue(validation.is_positive_number('299'))

    def test_invalidates_negative_number_case1(self):
        self.assertFalse(validation.is_positive_number(-299))

    def test_invalidates_negative_number_case2(self):
        self.assertFalse(validation.is_positive_number('abc'))

    def test_validates_binary(self):
        self.assertTrue(validation.is_valid_binary('101010001'))

    def test_invalidates_binary_case1(self):
        self.assertFalse(validation.is_valid_binary('101010001ab'))

    def test_invalidates_binary_case2(self):
        self.assertFalse(validation.is_valid_binary('a2bd'))

    def test_invalidates_binary_case3(self):
        self.assertFalse(validation.is_valid_binary(''))

    def test_validates_http_url(self):
        self.assertTrue(validation.is_valid_http_url('http://iprogrammerr.com'))

    def test_validates_https_url(self):
        self.assertTrue(validation.is_valid_http_url('https://www.youtube.com'))

    def test_invalidates_http_url(self):
        self.assertFalse(validation.is_valid_http_url('url'))
