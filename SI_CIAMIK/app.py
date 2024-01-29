import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import train_and_evaluate_model, read_data

# Fungsi untuk membaca data dari file CSV
def load_data(kelas):
    file_path = f"data/{kelas}.csv"
    data = pd.read_csv(file_path)
    return data

# Fungsi untuk menampilkan grafik dan daftar 3 nilai tertinggi
def display_data(data, semester):
    st.subheader("Grafik Indeks Prestasi Semester (IPS)")

    # Periksa apakah kolom semester yang dipilih ada dalam data
    if str(semester) not in data.columns:
        st.error("Data IPS tidak ditemukan, kelas Anda belum ujian!")
        return

    # Membuat grafik batang
    fig, ax = plt.subplots()
    data.plot(kind='bar', x='nama', y=str(semester), ax=ax, legend=False)
    ax.set_ylabel("IPS")
    ax.set_xlabel("Nama Taruna")
    st.pyplot(fig)

    st.subheader("Top 3 Nilai Tertinggi")

    # Menampilkan 3 nilai tertinggi
    top_three = data.nlargest(3, str(semester))[['nama', str(semester)]]
    st.table(top_three)

# Menambahkan tombol untuk prediksi semester selanjutnya
    if semester < 7:
        if st.button("Prediksi Si Ciamik"):
            next_semester = semester + 1

            # Menggunakan model linear regression untuk prediksi
            model = train_and_evaluate_model(X_train, y_train, X_val, y_val, X_test, y_test)['model']

            # Membaca data IPS untuk prediksi
            X_new_data = data[[str(i) for i in range(1, next_semester)]]

            # Melakukan prediksi
            predictions = model.predict(X_new_data)

            # Menampilkan hasil prediksi
            st.subheader(f"Prediksi Nilai IPS Semester {next_semester}")
            st.write("Nama Taruna:", data['nama'].tolist())
            st.write("Prediksi Nilai IPS:", predictions)

def main():
    st.title("Aplikasi Monitoring IPK dan Mentoring Akademik")

    # Dropdown untuk memilih kelas
    kelas = st.selectbox("Pilih Kelas", [
        "4RKSBLUE", "4RKSRED", "4RPK", "4RPLK", "4RSK",
        "3RKSECHO", "3RKSROUTE", "3RKSTRACE", "3RPK", "3RPLK", "3RSK",
        "2RKSA", "2RKSB", "2RPK", "2RPLK", "2RSKA", "2RSKB",
        "1RKSA", "1RKSB", "1RKSC", "1RPK", "1RPLK", "1RSK"
    ])

    # Dropdown untuk memilih semester
    semester = st.selectbox("Pilih Semester", [1, 2, 3, 4, 5, 6, 7])

    # Memuat data dari file CSV
    data = load_data(kelas)

    # Menampilkan grafik dan daftar 3 nilai tertinggi
    display_data(data, semester)

if __name__ == "__main__":
    main()