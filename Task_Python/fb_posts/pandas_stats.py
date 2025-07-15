import pandas as pd
import os

DATA_PATH = os.path.join('..', 'data', '2024_fb_posts_president_scored_anon.csv')
df = pd.read_csv(DATA_PATH)

print(f"\n Loaded {len(df)} rows and {len(df.columns)} columns.")

print("\n Descriptive Statistics (Numeric Columns):")
print(df.describe())

print("\n Unique Value Counts:")
for col in df.columns:
    unique_count = df[col].nunique()
    print(f"{col}: {unique_count} unique values")

print("\n Most Frequent Values (Categorical Columns):")
for col in df.select_dtypes(include='object').columns:
    most_common = df[col].value_counts().head(1)
    print(f"{col}: {most_common.index[0]} ({most_common.values[0]} times)")