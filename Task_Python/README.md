# Political Social Media Analysis — Python, Pandas & Polars

This project analyzes 2024 presidential Facebook and Twitter posts using three approaches: **pure Python**, **pandas**, and **polars**.

## Project Summary

This project analyzes three political social media datasets from the 2024 U.S. presidential campaign:

- 🟦 **Facebook Posts**
- 🟨 **Facebook Ads**
- 🐦 **Twitter Posts**

Each dataset is explored using three different approaches to demonstrate flexibility and performance tradeoffs:

- **Pure Python** – for low-level control and transparency  
- **Pandas** – for powerful and user-friendly data analysis  
- **Polars** – for faster, memory-efficient analytics on large datasets

All scripts include:
- Descriptive statistics  
- Unique value counts  
- Top value frequencies  
- Clean and modular code for easy extension

## 🛠️ How to Run

To run any script successfully:

**Navigate into the script folder** (e.g., `fb_posts/`, `fb_ads/`, or `twitter_posts/`) so that relative paths work properly:

   ```bash
   cd fb_ads
   ```

## 📥 Dataset Setup

Create `data/` folder in Task_Python and add the datasets to the folder manually.

You must download the original files from the following Google Drive link:

🔗 [Download Datasets](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

Once downloaded, place the following three files inside the `data/` directory:

- `2024_fb_posts_president_scored_anon.csv`  
- `2024_fb_ads_president_scored_anon.csv`  
- `2024_tw_posts_president_scored_anon.csv`  

## 📜 Code Overview:

- `pure_python.py`:  
  Loads and analyzes Facebook posts, twitter posts, Facebook ads using built-in tools.
  - **Functions Used**:  
    `open()`, `csv.DictReader`, `statistics.mean`, `statistics.median`, `Counter`, `defaultdict`, list comprehensions

- `pandas_stats.py`:  
  Uses `pandas` to analyze Facebook posts, twitter posts, Facebook ads data. 
  - **Functions Used**:  
    `pd.read_csv()`, `DataFrame.describe()`, `nunique()`, `value_counts()`, `select_dtypes()`

- `polars_stats.py`:  
  Replicates the same analysis using the faster `polars` library.
  - **Functions Used**:  
    `pl.read_csv()`, `df.describe()`, `n_unique()`, `group_by()`, `sort()`, `select()`, `pl.col(pl.datatypes.Utf8)`

---

**Install required libraries** (if not already installed):
   ```bash
   pip3 install pandas polars
   ```

## Learnings by Approach

### Pure Python
- Offers full control over file reading and data parsing.
- Good for learning how CSVs and dictionaries work internally.
- Slower and more verbose for large datasets.
- Requires manual handling of data types, missing values, and statistics.

### Pandas
- Very user-friendly and expressive for data analysis.
- Fast and efficient for medium-sized datasets.
- Rich set of built-in functions (`describe()`, `value_counts()`, `groupby()`).
- Easier to write and debug than pure Python, but can use more memory.

### Polars
- Extremely fast and memory-efficient, especially on large files.
- Syntax is slightly more functional and takes a bit of learning.
- Great for performance-critical analysis and large-scale processing.
- Still evolving, but quickly becoming a powerful alternative to pandas.

## 👨‍💻 Created By

**Asad Sajid Waghdhare**  
Master’s Student in Information Systems  
Syracuse University, Class of 2025
