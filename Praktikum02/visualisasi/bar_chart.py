import streamlit as st        # mengimpor library Streamlit untuk membuat aplikasi web interaktif
import pandas as pd           # mengimpor pandas untuk membuat dan mengelola data tabel
import numpy as np            # mengimpor numpy untuk menghasilkan data numerik acak

# === Judul Utama ===
st.title("Bar Chart")         # menampilkan judul utama pada halaman Streamlit

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")   # menampilkan subjudul
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")  # menampilkan daftar anggota kelompok dalam format markdown

# === Membuat DataFrame ===
df = pd.DataFrame(
    np.random.rand(40, 4),    # membuat 40 baris data acak dengan 4 kolom
    columns=["C1", "C2", "C3", "C4"]  # memberi nama kolom
)

# === Menampilkan Bar Chart ===
st.bar_chart(df)  # menampilkan data dalam bentuk grafik batang (bar chart)
