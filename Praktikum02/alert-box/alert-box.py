import streamlit as st  # mengimpor library streamlit

# === Judul Utama ===
st.title("Alert Box")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# Menampilkan berbagai jenis alert box di Streamlit
st.success("Successful")  # menampilkan pesan sukses (warna hijau)
st.warning("Warning")     # menampilkan pesan peringatan (warna kuning)
st.info("Info")           # menampilkan pesan informasi (warna biru)
st.error("Error")         # menampilkan pesan kesalahan (warna merah)
st.exception("It is an exception")  # menampilkan pesan exception (error Python)