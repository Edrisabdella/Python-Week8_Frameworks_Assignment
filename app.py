import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

@st.cache_data
def load_data():
    df = pd.read_csv('data/metadata.csv', low_memory=False)
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

year_range = st.slider("Select year range", 2019, 2023, (2019, 2022))
df = load_data()
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample Data")
st.dataframe(filtered.head(10))

st.subheader("Publications by Year")
fig, ax = plt.subplots()
filtered['year'].value_counts().sort_index().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader("Top Journals")
fig, ax = plt.subplots()
filtered['journal'].value_counts().head(10).plot(kind='barh', ax=ax)
st.pyplot(fig)

st.subheader("Word Cloud of Titles")
text = ' '.join(filtered['title'].dropna().astype(str))
if text.strip():
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10,4))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
else:
    st.write("Not enough title text to generate word cloud.")
