from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

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

    # Kirim data sebagai respons JSON
    return jsonify(data.to_dict(orient='records'))  # Mengubah format data sesuai kebutuhan frontend

# Definisikan route untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari frontend (Anda perlu menyesuaikan ini sesuai kebutuhan)
    data = request.get_json()

    model = joblib.load('mlp_regressor_model.joblib')
    
    # Lakukan prediksi menggunakan model (gantilah dengan model yang Anda miliki)
    predictions = model.predict(data['ips-now'])

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(port=5000)