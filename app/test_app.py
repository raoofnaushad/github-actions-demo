from main import return_backwards_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def setUp(self):
        self.test_string = "Hello World"
        self.rev_test_string = "dlroW olleH"

    def test_reverse_string(self):
        self.assertEqual(return_backwards_string(self.test_string), self.rev_test_string)

    def test_get_mode(self):
        self.assertEqual(get_mode(), get_mode())
        
        
if __name__ == '__main__':
    unittest.main()
    

        
        