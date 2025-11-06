import streamlit as st
import time


# === Judul Utama ===
st.title("Praktikum 4 - Buttons dan Sliders")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# === 1. Button ===
st.header("1. Button")
if st.button("Klik Saya"):  # tombol yang bisa ditekan
    st.success("Tombol telah ditekan!")  # aksi saat tombol ditekan

# === 2. Radio ===
st.header("2. Radio Button")
warna = st.radio("Pilih warna favorit:", ["Merah", "Hijau", "Biru"])  # pilihan tunggal
st.write("Warna pilihan kamu:", warna)

# === 3. Checkbox ===
st.header("3. Checkbox")
if st.checkbox("Saya setuju dengan syarat dan ketentuan"):  # kotak centang
    st.info("Kamu telah menyetujui!")  # aksi saat checkbox dicentang

# === 4. Selectbox ===
st.header("4. Selectbox (Dropdown)")
buah = st.selectbox("Pilih buah favorit:", ["Apel", "Jeruk", "Pisang", "Melon"])  # menu dropdown
st.write("Buah yang kamu pilih:", buah)

# === 5. Multiselect ===
st.header("5. Multiselect")
hobi = st.multiselect("Pilih hobi kamu:", ["Membaca", "Olahraga", "Menulis", "Musik", "Gaming"])
st.write("Hobi yang kamu pilih:", hobi)

# === 6. Download Button ===
st.header("6. Download Button")
csv_data = "Nama,Nilai\nAndi,90\nBudi,85\nCitra,88"  # data CSV sederhana
st.download_button("Download Data Nilai", csv_data, "nilai.csv", "text/csv")  # tombol download

# === 7. Slider ===
st.header("7. Slider")
nilai = st.slider("Pilih nilai dari 0 hingga 100:", 0, 100, 50)  # slider dengan default 50
st.write("Nilai yang kamu pilih:", nilai)

# === 8. Progress Bar dan Spinner ===
st.header("8. Progress Bar dan Spinner")
if st.button("Mulai Proses"):  # tombol untuk memulai proses
    with st.spinner("Proses sedang berjalan..."):  # spinner loading
        for i in range(101):
            st.progress(i)  # menampilkan progress bar
            time.sleep(0.02)  # simulasi proses berlangsung
    st.success("Proses selesai!")  # pesan sukses setelah loading selesai
