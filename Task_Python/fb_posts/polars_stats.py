import polars as pl
import os


DATA_PATH = os.path.join('..', 'data', '2024_fb_posts_president_scored_anon.csv')
df = pl.read_csv(DATA_PATH)

print(f"\n Loaded {df.shape[0]} rows and {df.shape[1]} columns.")


print("\n Descriptive Statistics (Numeric Columns):")
print(df.describe())


print("\n Unique Value Counts:")
for col in df.columns:
    unique_count = df[col].n_unique()
    print(f"{col}: {unique_count} unique values")


print("\n Most Frequent Values (Categorical Columns):")
for col in df.select(pl.col(pl.datatypes.Utf8)).columns:
    top = df.group_by(col).count().sort("count", descending=True).head(1)
    print(f"{col}: {top[col][0]} ({top['count'][0]} times)")