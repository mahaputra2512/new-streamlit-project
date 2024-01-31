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

def authenticate():
    password = st.text_input("Masukkan Password:", type="password")
    return password == "password123"  # Ganti dengan password yang diinginkan

def editing_ips():
    authenticated = authenticate()
    
    while not authenticated:
        st.warning("Password salah. Silakan coba lagi.")
        authenticated = authenticate()
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
    
    # Pilihan aksi
    action = st.radio("Pilih Aksi", ["Edit Data", "Tambah Data", "Hapus Data"])
    
    if action == "Edit Data":
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
    
    elif action == "Tambah Data":
        # Input data baru
        new_name = st.text_input("Masukkan Nama Taruna Baru")
        new_ips_values = st.text_input("Masukkan Nilai IPS (pisahkan dengan koma)")
        
        # Simpan perubahan saat tombol "Tambah Data" ditekan
        if st.button("Tambah Data"):
            # Pisahkan nilai IPS yang dimasukkan
            new_ips_list = [float(value.strip()) for value in new_ips_values.split(",")]
            
            # Buat data baru
            new_data = pd.DataFrame({"nama": [new_name], **{f"{i+1}": [ips] for i, ips in enumerate(new_ips_list)}, "ipk": [sum(new_ips_list) / len(new_ips_list)]})
            
            # Tambahkan data baru ke dataframe utama
            df = pd.concat([df, new_data], ignore_index=True)
            
            # Simpan perubahan ke file .csv
            save_data(df, file_path)
            
            # Tampilkan notifikasi
            st.success("Data baru berhasil ditambahkan!")
    
    elif action == "Hapus Data":
        # Pilihan nama taruna untuk dihapus
        selected_name_to_delete = st.selectbox("Pilih Nama Taruna yang Ingin Dihapus", df["nama"].tolist())
        
        # Simpan perubahan saat tombol "Hapus Data" ditekan
        if st.button("Hapus Data"):
            # Hapus baris dengan nama terpilih
            df = df[df["nama"] != selected_name_to_delete]
            
            # Simpan perubahan ke file .csv
            save_data(df, file_path)
            
            # Tampilkan notifikasi
            st.success("Data berhasil dihapus!")

if __name__:
    editing_ips()
