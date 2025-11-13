import streamlit as st 
import pandas as pd
import numpy as np

# === Judul Utama ===
st.title("Maps")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)