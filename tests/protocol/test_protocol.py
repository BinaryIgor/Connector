import unittest
from src.protocol.protocol import DataWithFormat, BINARY_FORMAT_PREFIX, \
    format_bytes

ENCODING = "utf8"


class TestProtocol(unittest.TestCase):

    def test_returns_text_bytes(self):
        text = 'abc'
        data = DataWithFormat(text)

        self.assertTrue(data.text)
        self.assertEqual(data.as_text_bytes(encoding=ENCODING),
                         bytes(text, encoding=ENCODING))

    def test_returns_binary_uneven_bytes(self):
        self._returns_binary_bytes('100', '10101111')

    def _returns_binary_bytes(self, first, second):
        data = DataWithFormat(BINARY_FORMAT_PREFIX + first + second)
        self.assertTrue(data.binary)
        self.assertEqual(data.as_binary_bytes(),
                         bytes([int(first, 2), int(second, 2)]))

    def test_returns_binary_even_bytes(self):
        self._returns_binary_bytes('10101000', '10101111')

    def test_raises_exception_on_empty_binary_bytes(self):
        msg = ''
        try:
            DataWithFormat(BINARY_FORMAT_PREFIX).as_binary_bytes()
        except Exception as e:
            msg = str(e)

        self.assertEqual(msg, 'Empty binary data')

    def test_returns_formatted_bytes(self):
        data = bytes([1, 4])
        self.assertEqual(format_bytes(data), '100000100')
