import unittest
from datetime import datetime

from analysis import compare_totals, summarise_activity
from preparation import filter_by_countries, filter_by_year_range
from records import EvaRecord


def eva(country, year, hours):
    date = datetime(year, 6, 1) if year else None
    return EvaRecord(country=country, date=date, duration_hours=hours)


RECORDS = [
    eva("USA", 1990, 6.0),
    eva("USA", 1995, 2.0),
    eva("USA", 2001, 5.0),   # after the period
    eva("USA", None, 3.0),   # undated, so never in a period
    eva("Russia", 1990, 4.0),
    eva("Russia", 2000, 3.0),
    eva("Russia", 1989, 9.0),  # before the period
]


def period_summary(country, start_year, end_year):
    period_records = filter_by_year_range(RECORDS, start_year, end_year)
    return summarise_activity(filter_by_countries(period_records, [country]))


class CountryComparisonTests(unittest.TestCase):
    def test_summary_for_each_country(self):
        self.assertEqual(period_summary("USA", 1990, 2000), {"count": 2, "total": 8.0, "average": 4.0})
        self.assertEqual(period_summary("Russia", 1990, 2000), {"count": 2, "total": 7.0, "average": 3.5})

    def test_equal_totals_is_a_tie(self):
        self.assertIsNone(compare_totals("USA", 5.0, "Russia", 5.0))


if __name__ == "__main__":
    unittest.main()
