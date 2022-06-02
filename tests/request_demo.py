import unittest
import requests


class RequestDemo(unittest.TestCase):
    def test_get_google(self):
        response = requests.get('http://www.google.com')
        self.assertEqual(200, response.status_code)  # add assertion here


if __name__ == '__main__':
    unittest.main()

