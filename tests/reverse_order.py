import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = "Roses are red and I am glad"
        expected_result = "glad am I red are Roses"

        output = self.reverse_string(input)
        self.assertEqual(expected_result, output)  # add assertion here

    def reverse_string(self, input: str):
        return ' '.join(list(reversed(input.split())))


if __name__ == '__main__':
    unittest.main()
