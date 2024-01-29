import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

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
    
    print("Cek data semester:")
    print(str(semester))

    # Membuat grafik batang
    fig, ax = plt.subplots()
    data.plot(kind='bar', x='nama', y=str(semester), ax=ax, legend=False)
    ax.set_ylabel("IPS")
    ax.set_xlabel("Nama Taruna")
    st.pyplot(fig)

    st.subheader("Peraih Sanapati Cendekia")

    # Menampilkan 3 nilai tertinggi
    top_three = data.nlargest(3, str(semester))[['nama', str(semester)]]
    st.table(top_three)

# Menambahkan tombol untuk prediksi semester selanjutnya
    if semester < 7:
        if st.button("Prediksi Si Ciamik"):
            next_semester = semester + 1
            st.success(f"Prediksi Grafik dan Peraih Sanapati Cendekia Semester {next_semester}")

            X_new_data = data[[str(semester)]]
            print("Ini:")
            print(X_new_data)

            # Melakukan prediksi
            model_path = "linear_regression_model.joblib"
            model = joblib.load(model_path)
            predictions = model.predict(X_new_data)

            print("Prediction:")
            print(predictions)

            # Menampilkan hasil prediksi
            st.subheader(f"Prediksi Nilai IPS Semester {next_semester}")
            # Menampilkan hasil prediksi dalam bentuk tabel
            predictions_table = pd.DataFrame({
                'Nama': data['nama'].tolist(),
                'Prediksi Nilai IPS': predictions.tolist()
            })

            fig, ax = plt.subplots()
            predictions_table.plot(kind='bar', x='Nama', y='Prediksi Nilai IPS', ax=ax, legend=False)
            ax.set_ylabel("Prediksi Nilai IPS")
            ax.set_xlabel("Nama Taruna")
            st.pyplot(fig)

            # Menampilkan top 3 nilai tertinggi
            top_three_indices = predictions.argsort()[-3:][::-1]
            top_three_names = data.iloc[top_three_indices]['nama'].tolist()
            top_three_predictions = predictions[top_three_indices]

            top_three_table = pd.DataFrame({
                'Nama Taruna': top_three_names,
                'Prediksi Nilai IPS': top_three_predictions
            })

            st.subheader("Prediksi Peraih Sanapati Cendekia Semester 2")
            st.table(top_three_table)

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