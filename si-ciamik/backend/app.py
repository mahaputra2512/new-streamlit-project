from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

def load_data(kelas):
    file_path = f"data/{kelas}.csv"
    data = pd.read_csv(file_path)
    return data

# Route untuk mengambil data berdasarkan kelas dan semester
@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # Ambil data dari body request
    req_data = request.get_json()
    kelas = req_data['kelas']
    semester = req_data['semester']

    # Memuat data dari file CSV
    data = load_data(kelas)

    # Lakukan sesuatu dengan hasil prediksi (misalnya, tampilkan di state atau komponen lain)
    # Implementasikan sesuai kebutuhan Anda

    # Kirim data sebagai respons JSON
    return jsonify(data.to_dict(orient='records'))

# Definisikan route untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari frontend (Anda perlu menyesuaikan ini sesuai kebutuhan)
    data = request.get_json()

    # Lakukan prediksi menggunakan model (gantilah dengan model yang Anda miliki)
    # predictions = model.predict(data['ips-now'])

    # Misalnya, kita mengembalikan contoh jawaban
    predictions = [4.0, 3.7, 3.5]

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(port=5000)