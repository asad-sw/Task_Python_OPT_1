import csv
import os
import statistics
from collections import defaultdict, Counter

DATA_PATH = os.path.join('..','data', '2024_tw_posts_president_scored_anon.csv')

def load_data(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

data = load_data(DATA_PATH)
print(f"\n Loaded {len(data)} rows.")

#Column names:

print("\n Column names:")
print(list(data[0].keys()))


numeric_columns = []
text_columns = []

sample_row = data[0]
for key, value in sample_row.items():
    try:
        float(value)
        numeric_columns.append(key)
    except (ValueError, TypeError):
        text_columns.append(key)


print("\n text names:")
print(text_columns)
print("\n numeric names:")
print(numeric_columns)

def describe_numeric(column):
    values = [float(row[column].replace(',', '')) for row in data if row[column]]
    count = len(values)
    mean = sum(values) / count if count else 0
    minimum = min(values) if values else None
    maximum = max(values) if values else None
    std_dev = statistics.stdev(values) if count > 1 else 0
    return {
        "count": count,
        "mean": mean,
        "min": minimum,
        "max": maximum,
        "std_dev": std_dev
    }


print("\n📊 --- Numeric Columns Summary ---")
for col in numeric_columns:
    stats = describe_numeric(col)
    print(f"\n🔹 {col}:\n{stats}")


def describe_text(column):
    values = [row[column] for row in data if row[column]]
    count = len(values)
    unique = len(set(values))
    most_common = Counter(values).most_common(1)[0] if values else ("None", 0)
    return {
        "count": count,
        "unique": unique,
        "most_common": most_common
    }

print("\n📝 --- Text Columns Summary ---")
for col in text_columns:
    stats = describe_text(col)
    print(f"\n🔸 {col}:\n{stats}")
