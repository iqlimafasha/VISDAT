import streamlit as st 

# === Judul Utama ===
st.title("Columns Chart")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/kucing.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("../../praktikum01/assets/kucing.jpg")