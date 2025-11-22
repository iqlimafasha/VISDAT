import streamlit as st  #type:ignore
import matplotlib.pyplot as plt  #type:ignore

# Buat data sample 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70] 
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout Streamlit 
st.title("Visualisasi Penjualan Product")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot", "Multiple & Customizations", "Jenis Garis untuk Menunjukkan Tren", "Subplot"))


# Identitas Kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 1:
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 0110222280
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A")
    ax.set_title('Penjualan Product A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    st.pyplot(fig)


# Multiple Line Plot & Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color="blue",
            linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color="red",
            linestyle='-', marker='x')

    ax.set_title('Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


# Fungsi tren_line_plot (dibuat terpisah, sesuai permintaan "tidak merubah struktur")
def tren_line_plot():
    # Data sample tambahan
    product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
    product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]

    fig, ax = plt.subplots()
    ax.plot(months, product_C_sales, label="Product C", color="green",
            linestyle='-.')
    ax.plot(months, product_D_sales, label="Product D", color="purple",
            linestyle=':')
    ax.set_title('Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


# Subplot
def subplots():
    product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
    product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]

    fig, axs = plt.subplots(2,1, figsize=(10,8))

    # plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Product C')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # plot kedua untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', color='purple', marker='s')
    axs[1].set_title('Penjualan Product D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)


# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()
