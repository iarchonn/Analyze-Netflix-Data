import streamlit as st
import pandas as pd

st.title("Analisis Data Netflix")

df = pd.read_csv("netflix_titles.csv")
# menampilkan table
st.write(df.head())

st.sidebar.header("Filter Data")

jenis_konetn = st.sidebar.selectbox("Pilih Jenis Konten", options=df['type'].unique())

min_tahun = int(df['release_year'].min())
max_tahun = int(df['release_year'].max())

tahun = st.sidebar.slider("Tahun Rilis", min_value=min_tahun, max_value=max_tahun)

filter_df = df[(df['type'] == jenis_konetn) & (df['release_year'] == tahun)]

st.subheader(f"Hasil Filter: {jenis_konetn} - Tahun {tahun}")
st.write(f"Jumlah Data: {filter_df.shape[0]}")
st.write(filter_df[['title','release_year','rating', 'duration']])

# menampilkan negara top 10
country_count = df['country'].value_counts().head(10)
st.bar_chart(country_count)