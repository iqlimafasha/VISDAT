import streamlit as st
import pandas as pd

# === Judul Utama ===
st.title("Praktikum 5 - Forms")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# === Membuat Satu Form Lengkap ===
with st.form("full_form"):
    st.subheader("Silakan lengkapi formulir di bawah ini:")

    # Input teks (Nama dan Password)
    name = st.text_input("Nama Lengkap", max_chars=10)  # input teks nama, maksimal 10 karakter
    password = st.text_input("Kata Sandi", type="password")  # input password

    # Text area (Deskripsi Diri)
    bio = st.text_area("Deskripsi Diri", placeholder="Tuliskan deskripsi singkat tentang diri Anda...")

    # Number input (Umur)
    umur = st.number_input("Umur", min_value=0, max_value=120, value=20, step=1)

    # Time input (Waktu)
    waktu = st.time_input("Pilih waktu saat mengisi form")

    # Date input (Tanggal lahir)
    tanggal_lahir = st.date_input("Tanggal Lahir")

    # Color picker (Warna favorit)
    warna = st.color_picker("Pilih warna favorit Anda", "#00f900")

    # File uploader (Upload gambar atau CSV)
    upload = st.file_uploader("Unggah foto profil atau file data (.csv)", type=["png", "jpg", "jpeg", "csv"])

    # Tombol submit
    submit = st.form_submit_button("Kirim Formulir")

# === Tindakan Setelah Form Dikirim ===
if submit:
    st.success("✅ Data berhasil dikirim!")

    # Menampilkan hasil input pengguna
    st.write("### Hasil Input:")
    st.write(f"**Nama:** {name}")
    st.write(f"**Kata Sandi:** {password}")
    st.write(f"**Deskripsi Diri:** {bio}")
    st.write(f"**Umur:** {umur}")
    st.write(f"**Waktu Pengisian:** {waktu}")
    st.write(f"**Tanggal Lahir:** {tanggal_lahir}")
    st.write(f"**Warna Favorit:** {warna}")

    # Menampilkan file upload jika ada
    if upload:
        if upload.type.startswith("image/"):
            st.image(upload, caption="Foto Profil yang Diupload", use_column_width=True)
        elif upload.name.endswith(".csv"):
            df = pd.read_csv(upload)
            st.dataframe(df)
    else:
        st.info("Tidak ada file yang diunggah.")
