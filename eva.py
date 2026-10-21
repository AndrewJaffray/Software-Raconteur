
import analysis
import presentation
from data_loader import load_eva_data
from preparation import filter_by_countries, filter_by_year_range, parse_year_range, prepare_records


def compare_period(records, first_country, second_country):
    year_range = parse_year_range(input("Enter the start year: "), input("Enter the end year: "))
    if year_range is None:
        presentation.print_message("Invalid year range.")
        return

    start_year, end_year = year_range
    period_records = filter_by_year_range(records, start_year, end_year)

    presentation.print_period_heading(start_year, end_year)
    summaries = {}
    for country in (first_country, second_country):
        summaries[country] = analysis.summarise_activity(filter_by_countries(period_records, [country]))
        presentation.print_activity_summary(country, summaries[country])

    winner = analysis.compare_totals(
        first_country, summaries[first_country]["total"],
        second_country, summaries[second_country]["total"],
    )
    presentation.print_comparison(winner)


def main():
    records = prepare_records(load_eva_data())

    first_country = input("Enter the first country to report: ").strip()
    second_country = input("Enter the second country to report: ").strip()
    countries = (first_country, second_country)

    totals = {
        country: analysis.total_duration(filter_by_countries(records, [country]))
        for country in countries
    }
    for country in countries:
        presentation.print_total(country, totals[country])

    for country in countries:
        counts = analysis.categorise_durations(filter_by_countries(records, [country]))
        presentation.print_categories(country, counts, analysis.category_percentages(counts))

    winner = analysis.compare_totals(first_country, totals[first_country], second_country, totals[second_country])
    presentation.print_comparison(winner)

    compare_period(records, first_country, second_country)

    dates, cumulative_hours = analysis.cumulative_series(filter_by_countries(records, countries))
    presentation.plot_cumulative(dates, cumulative_hours)


if __name__ == "__main__":
    main()
