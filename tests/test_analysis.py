import unittest

from analysis import categorise_durations
from records import EvaRecord


def eva(hours):
    return EvaRecord(country="USA", date=None, duration_hours=hours)


class ExistingAnalysisTests(unittest.TestCase):
    def test_categorise_durations(self):
        records = [eva(0.5), eva(3.9), eva(4.0), eva(6.9), eva(7.0), eva(8.5)]
        self.assertEqual(categorise_durations(records), {"Short": 2, "Standard": 2, "Long": 2})


if __name__ == "__main__":
    unittest.main()
