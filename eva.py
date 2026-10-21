
import analysis
import presentation
from data_loader import load_eva_data
from preparation import filter_by_countries, prepare_records


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

    dates, cumulative_hours = analysis.cumulative_series(filter_by_countries(records, countries))
    presentation.plot_cumulative(dates, cumulative_hours)


if __name__ == "__main__":
    main()
