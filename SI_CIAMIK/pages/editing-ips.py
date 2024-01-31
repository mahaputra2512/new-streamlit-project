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
    st.title("Edit Data IPS")
    
    # Pilihan file .csv
    selected_file = st.selectbox("Pilih File CSV", ["4RKSBLUE.csv", "4RKSRED.csv", "4RPLK.csv", "4RPK.csv", "4RSK.csv",
                                                    "3RKSECHO.csv", "3RKSROUTE.csv", "3RKSTRACE.csv", "3RPLK.csv", "3RPK.csv", "3RSK.csv",
                                                    "2RKSA.csv", "2RKSB.csv", "2RPLK.csv", "2RPK.csv", "2RSKA.csv", "2RSKB.csv",
                                                    "1RKSA.csv", "1RKSB.csv", "1RKSC.csv", "1RPLK.csv", "1RPK.csv", "1RSK.csv"])
    
    # Baca data dari file .csv
    file_path = os.path.join("data", selected_file)
    df = load_data(file_path)
    
    # Tampilkan seluruh data taruna sebelum diedit
    st.write("Seluruh Data Taruna Sebelum Diedit:", df)
    
    # Pilihan nama taruna
    selected_name = st.selectbox("Pilih Nama Taruna", df["nama"].tolist())
    
    # Pilihan kolom untuk diedit
    selected_column = st.selectbox("Pilih Kolom yang Ingin Diedit", df.columns[1:-1])
    
    # Input nilai IPS baru
    new_ips = st.number_input(f"Masukkan Nilai IPS Baru untuk {selected_column}", min_value=0.0, max_value=4.0, step=0.01)
    
    # Simpan perubahan saat tombol "Simpan Perubahan" ditekan
    if st.button("Simpan Perubahan"):
        # Update nilai IPS pada data
        df.loc[df["nama"] == selected_name, selected_column] = new_ips
        
        # Hitung nilai IPK baru
        df["ipk"] = df.iloc[:, 1:-1].mean(axis=1)
        
        # Simpan perubahan ke file .csv
        save_data(df, file_path)
        
        # Tampilkan notifikasi
        st.success("Perubahan berhasil disimpan!")

if __name__:
    editing_ips()