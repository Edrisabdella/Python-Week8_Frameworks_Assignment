import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter

# Set page configuration
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    
    # Data cleaning
    df_clean = df.copy()
    df_clean = df_clean.drop(['who_covidence_id', 'arxiv_id', 'pmcid', 'mag_id', 's2_id'], axis=1)
    df_clean['abstract'] = df_clean['abstract'].fillna('')
    df_clean['authors'] = df_clean['authors'].fillna('Unknown')
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean['year'] = df_clean['publish_time'].dt.year
    df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))
    
    return df_clean

# Load the data
df = load_data()

# Title and description
st.title("CORD-19 Data Explorer")
st.write("""
This application provides an interactive exploration of the CORD-19 dataset, 
which contains metadata about COVID-19 research papers.
""")

# Sidebar with filters
st.sidebar.header("Filters")

# Year range selector
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Journal selector
journals = df['journal'].dropna().unique()
selected_journals = st.sidebar.multiselect(
    "Select journals",
    options=journals,
    default=journals[:5] if len(journals) > 5 else journals
)

# Apply filters
filtered_df = df[
    (df['year'] >= year_range[0]) & 
    (df['year'] <= year_range[1]) &
    (df['journal'].isin(selected_journals) if selected_journals else True)
]

# Display dataset info
st.header("Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Papers", df.shape[0])
col2.metric("Filtered Papers", filtered_df.shape[0])
col3.metric("Columns", df.shape[1])

# Show filtered data
if st.checkbox("Show filtered data"):
    st.write(filtered_df.head(10))

# Visualizations
st.header("Visualizations")

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
year_counts.plot(kind='bar', ax=ax)
ax.set_title('Number of Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Journals by Number of Publications')
ax.set_xlabel('Journal')
ax.set_ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(fig)

# Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
all_titles = ' '.join(filtered_df['title'].dropna().values)
if all_titles.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud of Paper Titles')
    st.pyplot(fig)
else:
    st.write("No titles available for the selected filters.")

# Abstract word count distribution
st.subheader("Abstract Word Count Distribution")
fig, ax = plt.subplots()
filtered_df['abstract_word_count'].hist(bins=50, ax=ax)
ax.set_title('Distribution of Abstract Word Count')
ax.set_xlabel('Word Count')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Most common words in titles
st.subheader("Most Common Words in Titles")
all_titles = ' '.join(filtered_df['title'].dropna().values)
words = re.findall(r'\w+', all_titles.lower())
word_freq = Counter(words)
common_words = word_freq.most_common(20)

common_words_df = pd.DataFrame(common_words, columns=['Word', 'Count'])
fig, ax = plt.subplots()
common_words_df.plot(kind='bar', x='Word', y='Count', ax=ax)
ax.set_title('Top 20 Words in Titles')
ax.set_xlabel('Word')
ax.set_ylabel('Frequency')
plt.xticks(rotation=45)
st.pyplot(fig)

# Additional insights
st.header("Additional Insights")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Papers with Missing Abstracts")
    missing_abstracts = filtered_df['abstract'].isna().sum()
    st.metric("Count", missing_abstracts)

with col2:
    st.subheader("Average Abstract Length")
    avg_length = filtered_df['abstract_word_count'].mean()
    st.metric("Words", f"{avg_length:.2f}")

# Footer
st.markdown("---")
st.markdown("CORD-19 Data Explorer | Created with Streamlit")