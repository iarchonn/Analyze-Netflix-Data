import streamlit as st
import pandas as pd

st.title("Analisis Data Netflix")

df = pd.read_csv("netflix_titles.csv")
# menampilkan table
st.write(df.head(10))

st.sidebar.header("Filter Data")

jenis_konten = st.sidebar.selectbox("Pilih Jenis Konten", options=df['type'].unique())

min_tahun = int(df['release_year'].min())
max_tahun = int(df['release_year'].max())

pilih_rating = st.sidebar.selectbox("Pilih Rating Konten", options=df['rating'].unique())

tahun = st.sidebar.slider("Tahun Rilis", min_value=min_tahun, max_value=max_tahun)

filter_df = df[(df['type'] == jenis_konten) & (df['release_year'] == tahun) & (df['rating'] == pilih_rating)]

st.subheader(f"Hasil Filter: {jenis_konten} - Tahun {tahun} & {pilih_rating}")
st.write(f"Jumlah Data: {filter_df.shape[0]}")
st.write(filter_df[['title','release_year','rating', 'duration']])

st.write("Grafik umlah Konten per Rating")

rating_count = df["rating"].value_counts().sort_values(ascending=False)

st.bar_chart(rating_count)

# menampilkan negara top 10
country_count = df['country'].dropna().str.split(',').explode().value_counts().sort_values(ascending=False)
st.bar_chart(country_count.head(10))

st.subheader("Grafik Genre Terpopuler (Top 10)")
genre_series = df['listed_in'].dropna().str.split(', ').explode()
genre_count = genre_series.value_counts().sort_index().head(10)

st.bar_chart(genre_count)