#import library
import streamlit as st 
import pandas as pd  #untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np #untuk membuat data numerik acak
import altair as alt  #untuk membuat chart interaktif

# DataFrame: struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn (30,10),
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan dataframe
st.dataframe(df)

#Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

#Highlight nilai terkecil di setiap kolom dataframe 
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn (30,10),
    columns=('col_no %d' % i for i in range (10))
)
#menampilkan tabel statis
st.table(df)

#Metrics: 
st.subheader("Metrics")
#Menampilkan metrik tunggal (nilai utama + perubahan nilai)

#metrics tunggal
st.metric(label="Temperatur", value="31 C", delta="1,2 C") 
#kenaikan 1.2 C


# metrics sesuai delta_color
# delta_color digunakna untuk memberi warna sesuai arah perubahan
# delta_color digunakan untuk memberi warna sesuai arah peruwanan:
# - 'default' (default): naik -> hijau, turun -> merah
# - 'normal': kebalikannya (naik -> merah)
# - 'inverse': kebalikannya (naik -> merah)
# - 'off': tidak menampilkan warna perubahan


#definisikan variabel metrics
col1, col2, col3 = st.columns(3)

#menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off") #netral (tidak baik, tidak buruk)

st.metric(label="Speed", value=None, delta=0) #kosong 3naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan