import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('metadata.csv', low_memory=False)
print(f"Dataset shape: {df.shape}")

# Basic exploration
print("\n=== BASIC EXPLORATION ===")
print("First few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False)[:10])  # Top 10 columns with most missing values

# Data cleaning
print("\n=== DATA CLEANING ===")
# Handle missing values
df_clean = df.copy()
# Drop columns with too many missing values
df_clean = df_clean.drop(['who_covidence_id', 'arxiv_id', 'pmcid', 'mag_id', 's2_id'], axis=1)
# Fill missing abstracts with empty string
df_clean['abstract'] = df_clean['abstract'].fillna('')
# Fill missing authors with 'Unknown'
df_clean['authors'] = df_clean['authors'].fillna('Unknown')
# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
# Extract year from publish_time
df_clean['year'] = df_clean['publish_time'].dt.year
# Create abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))

print("Data cleaning completed. New shape:", df_clean.shape)

# Analysis
print("\n=== ANALYSIS ===")
# Papers by year
papers_by_year = df_clean['year'].value_counts().sort_index()
print("Papers by year:")
print(papers_by_year)

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
print("\nTop 10 journals:")
print(top_journals)

# Most frequent words in titles
all_titles = ' '.join(df_clean['title'].dropna().values)
words = re.findall(r'\w+', all_titles.lower())
word_freq = Counter(words)
common_words = word_freq.most_common(20)
print("\nMost common words in titles:")
print(common_words)

# Visualization
print("\n=== VISUALIZATION ===")
# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Plot publications over time
plt.figure()
papers_by_year.plot(kind='bar')
plt.title('Number of Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('publications_by_year.png')
print("Saved publications_by_year.png")

# Plot top journals
plt.figure()
top_journals.plot(kind='bar')
plt.title('Top 10 Journals by Number of Publications')
plt.xlabel('Journal')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_journals.png')
print("Saved top_journals.png")

# Word cloud of titles
plt.figure()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.tight_layout()
plt.savefig('wordcloud_titles.png')
print("Saved wordcloud_titles.png")

# Distribution of abstract word count
plt.figure()
df_clean['abstract_word_count'].hist(bins=50)
plt.title('Distribution of Abstract Word Count')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('abstract_word_count.png')
print("Saved abstract_word_count.png")

print("\nAnalysis completed successfully!")