import unittest
from datetime import datetime

from preparation import filter_by_year_range, parse_year_range
from records import EvaRecord


class YearRangeTests(unittest.TestCase):
    def test_start_after_end_is_invalid(self):
        self.assertIsNone(parse_year_range("2000", "1990"))

    def test_range_includes_start_and_end_years(self):
        records = [
            EvaRecord("USA", datetime(1989, 12, 31), 1.0),
            EvaRecord("USA", datetime(1990, 1, 1), 1.0),
            EvaRecord("USA", datetime(2000, 12, 31), 1.0),
            EvaRecord("USA", datetime(2001, 1, 1), 1.0),
        ]
        years = [record.date.year for record in filter_by_year_range(records, 1990, 2000)]
        self.assertEqual(years, [1990, 2000])


if __name__ == "__main__":
    unittest.main()
