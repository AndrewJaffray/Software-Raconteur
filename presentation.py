
import matplotlib.pyplot as plt


def print_total(country, total_hours):
    print(f"Total EVA duration for {country}: {total_hours:.2f} hours")


def print_categories(country, counts, percentages):
    print(f"EVA duration categories for {country}:")
    for category, count in counts.items():
        print(f"  {category}: {count} ({percentages[category]:.2f}%)")


def print_comparison(winner):
    if winner is None:
        print("Both countries have the same total EVA duration.")
    else:
        print(f"{winner} has the greater total EVA duration.")


def print_period_heading(start_year, end_year):
    print(f"EVA activity from {start_year} to {end_year}:")


def print_activity_summary(country, summary):
    if summary["average"] is None:
        average = "unavailable"
    else:
        average = f"{summary['average']:.2f} hours"
    print(f"  {country}: {summary['count']} EVAs, "
          f"total {summary['total']:.2f} hours, average {average}")


def print_message(message):
    print(message)


def plot_cumulative(dates, cumulative_hours, output_path="cumulative_duration.png"):
    plt.plot(dates, cumulative_hours)
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
