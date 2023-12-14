#Testingproject3 program
import unittest
from unittest.mock import patch
from Project3 import imput_member_id


class TestProject3(unittest.TestCase):

    @patch('builtins.input', return_value='123')
    def test_imput_member_id_valid_input(self, mock_input):
        result = imput_member_id()
        self.assertEqual(result, 123)

    @patch('builtins.input', side_effect=['abc', '456', '789'])
    def test_imput_member_id_invalid_input_then_valid_input(self, mock_input):
        result = imput_member_id()
        self.assertEqual(result, 456)

    @patch('builtins.input', side_effect=['abc', 'def', 'ghi'])
    def test_imput_member_id_invalid_input_multiple_times(self, mock_input):
        result = imput_member_id()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()