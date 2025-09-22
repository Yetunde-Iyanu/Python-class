# PART:- Data Loading and Basic Exploration
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("metadata.csv")
# Examining the first few rows and data structure
print(df.head())
# Check the DataFrame dimensions (rows, columns)
print("Shape:", df.shape)

# Identifing data types of each colum
print(df.dtypes)

# Checking for missing values in important columns
print(df.isnull().sum().head(20))

# Generating basic statistics for numerical columns
print(df.describe())


#PART 2:- 
# Handle missing values
# Drop rows missing essential info like title or publish_time
df_clean = df.dropna(subset=["title", "publish_time"]).copy()

# FillING missing journal names with "Unknown"
df_clean["journal"] = df_clean["journal"].fillna("Unknown")

# Convert publish_time to datetime
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")

# ExtractING year
df_clean["year"] = df_clean["publish_time"].dt.year

# CreatING abstract word count column
df_clean["abstract_word_count"] = df_clean["abstract"].fillna("").apply(lambda x: len(x.split()))


#PART3:- Data Analysis and Visualization
# Handle dates
if "publish_time" in df.columns:
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year

# TiFind most frequent words in titles
st.title("CORD-19 Data Explorer - Analysis & Visualization")

# Plot number of publications over time
if "year" in df.columns:
    st.subheader("Publications per Year")
    fig, ax = plt.subplots()
    df["year"].value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.set_title("Publications per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Creating a bar chart of top publishing journals
if "journal" in df.columns:
    st.subheader("Top Journals Publishing COVID-19 Papers")
    top_journals = df["journal"].fillna("Unknown").value_counts().head(10)
    fig, ax = plt.subplots()
    top_journals.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Journals")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Generate a word cloud of paper titles
if "title" in df.columns:
    st.subheader("Word Cloud of Paper Titles")
    text = " ".join(str(t) for t in df["title"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Ploting distribution of paper counts by source
if "source_x" in df.columns:
    st.subheader("Distribution of Papers by Source")
    fig, ax = plt.subplots()
    df["source_x"].value_counts().head(10).plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Sources")
    st.pyplot(fig)


# Plot number of publications over time
    st.subheader("Top Journals Publishing COVID-19 Papers")
    top_journals = df["journal"].fillna("Unknown").value_counts().head(10)
    fig, ax = plt.subplots()
    top_journals.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Journals")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Generate a word cloud of paper titles
if "title" in df.columns:
    st.subheader("Word Cloud of Paper Titles")
    text = " ".join(str(t) for t in df["title"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Plot distribution of paper counts by source
    st.subheader("Distribution of Papers by Source")
    fig, ax = plt.subplots()
    df["source_x"].value_counts().head(10).plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Sources")
    st.pyplot(fig)

# PART 4:- Streamlit Application
# Covid_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["journal"] = df["journal"].fillna("Unknown")
    return df

df = load_data()
# Streamlit App Layout 
st.title("CORD-19 Data Explorer")
st.write("A simple exploration of COVID-19 research papers (CORD-19 dataset).")

# Sidebar filters
st.sidebar.header("Filters")
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.sidebar.slider("Select year range", year_min, year_max, (2020, 2021))
df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show sample of the data
st.subheader("Sample Data")
st.write(df_filtered.head())

# Publications over time
st.subheader("Publications Over Time")
pubs_by_year = df_filtered["year"].value_counts().sort_index()
st.bar_chart(pubs_by_year)

# Top journals
st.subheader("Top Publishing Journals")
top_journals = df_filtered["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud
st.subheader("Word Cloud of Titles / Abstracts")
text_source = st.radio("Choose text source", ["title", "abstract"])
text_data = " ".join(df_filtered[text_source].dropna().astype(str))

if text_data:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("No text available for word cloud.")
