
from datetime import datetime
from records import EvaRecord


def normalise_country(name):
    return name.strip().casefold()


def parse_duration(duration_text):
    if not duration_text:
        return None
    try:
        hours, minutes = map(int, duration_text.split(":"))
    except ValueError:
        return None
    return hours + minutes / 60


def parse_date(date_text):
    if not date_text:
        return None
    try:
        return datetime.fromisoformat(date_text)
    except ValueError:
        return None


def prepare_records(raw_data):
    records = []
    for eva in raw_data:
        duration_hours = parse_duration(eva.get("duration"))
        if duration_hours is None:
            continue
        records.append(EvaRecord(
            country=eva.get("country", "").strip(),
            date=parse_date(eva.get("date")),
            duration_hours=duration_hours,
        ))
    return records


def filter_by_countries(records, countries):
    wanted = {normalise_country(country) for country in countries}
    return [record for record in records if normalise_country(record.country) in wanted]


def parse_year_range(start_text, end_text):
    try:
        start_year, end_year = int(start_text), int(end_text)
    except ValueError:
        return None
    if start_year > end_year:
        return None
    return start_year, end_year


def filter_by_year_range(records, start_year, end_year):
    return [
        record for record in records
        if record.date and start_year <= record.date.year <= end_year
    ]
