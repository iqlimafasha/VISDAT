import streamlit as st 
import graphviz as graphviz

# === Judul Utama ===
st.title("Graphis Visualisasi")

# === Identitas Kelompok ===
st.subheader("Anggota Kelompok 1:")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm" 
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")