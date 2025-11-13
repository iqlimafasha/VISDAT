import streamlit as st        # mengimpor library Streamlit untuk membuat aplikasi web interaktif
import pandas as pd           # mengimpor pandas untuk membuat dan mengelola data tabel
import numpy as np            # mengimpor numpy untuk menghasilkan data numerik acak

# === Judul Utama ===
st.title("Line Chart")        # menampilkan judul utama aplikasi Streamlit

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")   # menampilkan subjudul untuk identitas
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")  # menampilkan daftar anggota kelompok dalam format markdown

# === Membuat DataFrame ===
df = pd.DataFrame(
    np.random.randn(40, 4),   # membuat 40 baris data acak (berdistribusi normal) dengan 4 kolom
    columns=["C1", "C2", "C3", "C4"]  # menamai kolom dengan label C1 sampai C4
)

# === Menampilkan Line Chart ===
st.line_chart(df)  # menampilkan grafik garis berdasarkan data dari DataFrame
