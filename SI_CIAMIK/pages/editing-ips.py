import streamlit as st
import pandas as pd
import os

# Fungsi untuk membaca data dari file CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Fungsi untuk menyimpan perubahan ke file CSV
def save_data(data, file_path):
    data.to_csv(file_path, index=False)

def editing_ips():
    # Menampilkan judul
    st.title("Edit Data CSV dengan Streamlit")

    # Direktori tempat data CSV disimpan
    data_directory = "data"

    # Membaca semua file CSV dari direktori data/
    files = [f for f in os.listdir(data_directory) if f.endswith(".csv")]

    # Memilih file dari daftar file
    selected_file = st.selectbox("Pilih file CSV", files)

    # Membaca data dari file CSV yang dipilih
    file_path = os.path.join(data_directory, selected_file)
    df = load_data(file_path)

    # Memilih nama taruna
    selected_name = st.selectbox("Pilih Nama Taruna", df["nama"].tolist())

    # Memilih kolom
    selected_column = st.selectbox("Pilih Kolom", df.columns[1:-1])

    # Menampilkan form untuk mengubah nilai IPS
    new_ips = st.number_input(f"Masukkan nilai IPS untuk {selected_column}", value=df[df["nama"]==selected_name][selected_column].values[0])

    # Menyimpan perubahan jika tombol ditekan
    if st.button("Simpan Perubahan"):
        # Memperbarui nilai IPS pada DataFrame
        df.loc[df["nama"]==selected_name, selected_column] = new_ips
        
        # Menghitung IPK baru
        df["ipk"] = df.iloc[:, 1:-1].mean(axis=1)
        
        # Menyimpan perubahan ke file CSV
        save_data(df, file_path)
        
        st.success("Perubahan berhasil disimpan!")
        
        # Menampilkan data terbaru
        st.write("Data terbaru:")
        st.table(df)

if __name__:
    editing_ips()