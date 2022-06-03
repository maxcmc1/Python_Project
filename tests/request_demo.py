import unittest
import requests


class RequestDemo(unittest.TestCase):
    def test_get_google(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        header = {'user-agent': user_agent}

        response = requests.get('http://www.google.com', headers=header)
        self.assertEqual(200, response.status_code)  # add assertion here
        file = open("result.html", "w")
        file.write(response.text)
        file.close()


if __name__ == '__main__':
    unittest.main()

