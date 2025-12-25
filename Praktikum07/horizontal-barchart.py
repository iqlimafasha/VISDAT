import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

# judul
st.title("Praktikum 7 Visualisasi Data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

# identitas kelompok
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# Dataset
brand = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 280]
sales_2024 = [380, 450, 320, 300]

# atur posisi y
y = np.arange(len(brands))
bar_width = 0.4

# filter kategori
kategori = st.selectbox(
    "Pilih kategori visualisasi",
    ['Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

# Basic Bar Chart
if kategori == "Basic Bar Chart":
    st.subheader("Horizontal Bar Chart Sederhana")
    fig1, ax1, = plt.subplots()

    # grafik batang horizontal
    ax1.set_yticks (y)
    ax1.set_yticklabels(brands)
    ax1.set_title('Horizontal Bar Chart - 2023')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    ax1.barh(y, sales_2023, color='skyblue')
    st.pyplot(fig1)

    # stacked
    st.subheader("Stacked Horizontal Bar Chart Sederhana")
    fig2, ax2, = plt.subplots()
    ax2.set_yticks (y)
    ax2.set_yticklabels(brands)
    ax2.set_title('Horizontal Bar Chart - 2023')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(y, sales_2023, color='skyblue', label='2023')
    ax2.barh(y, sales_2024, color='lightgreen', label='2024', left=sales_2023)
    ax2.legend()
    st.pyplot(fig2)

    # kustomisasi
elif kategori == "Kustomisasi Grafik":
    st.subheader("Kustomisasi Horizontal Bar Chart")
    fig3, ax3, = plt.subplots()
    ax3.set_yticks (y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Horizontal Bar Chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='lightblue', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    #label nilai
    for i, v in enumerate(sales_2023):
        ax3.text(v+5, i, str(v), va='center')
    st.pyplot(fig3)

    #stacked
    st.subheader("Kustomisasi Horizontal Bar Chart")
    fig4, ax4, = plt.subplots()
    ax4.set_yticks (y)
    ax4.set_yticklabels(brands)
    ax4.set_title('Kustomisasi Bar Chart - 2023')
    ax4.set_xlabel('Jumlah Penjualan')
    ax4.set_ylabel('Merk')
    ax4.barh(y, sales_2023, label='2023', color='skyblue', edgecolor='black')a
    ax4.barh(y, sales_2024, label='2024', color='skyblue', edgecolor='black')
    ax4.grid(axis='x', linestyle='--', alpha=0.6)
    st.pyplot(fig)