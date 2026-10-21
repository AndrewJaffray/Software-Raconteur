
SHORT_LIMIT_HOURS = 4
LONG_LIMIT_HOURS = 7


def total_duration(records):
    return sum(record.duration_hours for record in records)


def categorise_duration(duration_hours):
    if duration_hours < SHORT_LIMIT_HOURS:
        return "Short"
    if duration_hours < LONG_LIMIT_HOURS:
        return "Standard"
    return "Long"


def categorise_durations(records):
    counts = {"Short": 0, "Standard": 0, "Long": 0}
    for record in records:
        counts[categorise_duration(record.duration_hours)] += 1
    return counts


def category_percentages(counts):
    total_evas = sum(counts.values())
    return {
        category: count / total_evas * 100 if total_evas else 0
        for category, count in counts.items()
    }


def count_evas(records):
    return len(records)


def average_duration(records):
    if not records:
        return None
    return total_duration(records) / count_evas(records)


def summarise_activity(records):
    return {
        "count": count_evas(records),
        "total": total_duration(records),
        "average": average_duration(records),
    }


def compare_totals(country_a, total_a, country_b, total_b):
    if total_a > total_b:
        return country_a
    if total_b > total_a:
        return country_b
    return None


def cumulative_series(records):
    dated = sorted((record for record in records if record.date), key=lambda record: record.date)
    dates = []
    cumulative_hours = []
    running_total = 0
    for record in dated:
        running_total += record.duration_hours
        dates.append(record.date)
        cumulative_hours.append(running_total)
    return dates, cumulative_hours
