import streamlit as st  # mengimpor library streamlit

# === Judul Utama ===
st.title("Sidebar")  # membuat judul pada panel sidebar

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# Elemen input di dalam sidebar
st.sidebar.radio("Are you a New User?", ["Yes", "No"])  # membuat pilihan radio button
st.sidebar.slider("Select a Number", 0, 10)  # membuat slider dari 0 sampai 10

# === Konten utama di halaman ===
st.title("Praktikum 4 - Sidebar di Streamlit")
st.write("Sidebar digunakan untuk menampilkan elemen interaktif di sisi aplikasi.")