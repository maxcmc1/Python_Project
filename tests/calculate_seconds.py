import unittest


class CalculateSecondsTestCase(unittest.TestCase):

    def test_non_zero_seconds_and_minutes(self):
        minutes = 3
        hours = 1
        expected_seconds = 3780
        actual_seconds = self.get_seconds(hours, minutes)
        self.assertEqual(expected_seconds, actual_seconds)  # add assertion here

    def test_negative_minutes(self):
        minutes = -3
        hours = 1
        expected_seconds = "The provided input '{0}' for minutes is not valid, please enter a positive number".format(minutes)
        actual_seconds = self.get_seconds(hours, minutes)
        self.assertEqual(expected_seconds, actual_seconds)  # add assertion here

    def test_negative_hours(self):
        minutes = 1
        hours = -5
        expected_seconds = "The provided input '{0}' for hours is not valid, please enter a positive number".format(hours)
        try:
            self.get_seconds(hours, minutes)
        except TypeError as e:
            self.assertEqual(expected_seconds, str(e))  # add assertion here

    def get_seconds(self, hours, minutes):
        if minutes < 0:
            return "The provided input '{0}' for minutes is not valid, please enter a positive number".format(minutes)
        if hours < 0:
            raise TypeError("The provided input '{0}' for hours is not valid, please enter a positive number".format(hours))

        return (hours * 60 + minutes) * 60


if __name__ == '__main__':
    unittest.main()
