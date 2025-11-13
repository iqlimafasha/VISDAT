#import library yang dibutuhkan
import streamlit as st

#text element
#header - untuk membuat tulisan header
st.header("Ini header") #untuk membuat header
st.subheader("ini sub header") #untuk membuat subjudul yang lebih kecil
st.text("ini teks biasa tanpa format") #untuk membuat teks polos tanpa format
st.markdown("**ini teks bold** dan *ini teks italic*") #markdown untuk memformat teks tebal/miring
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
*ini baris 3
*ini menggunakan markdown multibaris
""")


st.caption("ini caption") #teks kecil dibawah elemen (untuk penjelasan)
st.title("Ini judul")

#coba mandiri
#tuliskan:
#1. Judul praktikum pakai judul
#2. Bagian praktikum pakai subheader
#3. nama lengkap anggota - nim pakai markdown multibaris """"


st.title("PRAKTIKUM 01")
st.subheader("Ini tugas praktikum pertama")
st.markdown("""
1. Iqlima Fasha Rizqia - 0110122006
2. Muhammad Zidan - 011
""")


#bagian 2: Menampilkan Rumus (LaTex)
st.subheader("Displaying LaTex")
st.latex(r''' \cos'^\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binominal

#bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

#simpan ke variabel
code = '''
def hello();
    print ("Hello, Streamlit!)
'''

#st.code() untuk menampilkan potongan kode dengan format rapi dan syintax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello World!);
            }
        }
""", language='java')
#Fungsi st.code()bisa digunakan untuk bahasa pemrograman lain seperti java, javascriptt, c++, HTML, dll

st.subheader("JavaScript Code")
st.code("""
<script>
try {
    addalert("Welcome guest!); // kesalahan ketik (addalert) 
    sengaja dibuat untuk menimbulkan error
    }
    catch(err) {
    document.getElementById("demo").innerHTML = err.message; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
    }
    </script>
""", language='javascript')

#kode ini menunjukkan contoh bagaimana menangani error (excaption) di javascript
#Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh kode.

