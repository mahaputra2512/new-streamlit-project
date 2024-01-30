import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

def read_data(file_path, target_column='ips-next', feature_columns=None):
    df = pd.read_csv(file_path)

    # Jika feature_columns tidak ditentukan, ambil semua kolom kecuali target_column
    if feature_columns is None:
        feature_columns = df.columns[df.columns != target_column]

    # Pastikan kolom target dan fitur benar-benar ada dalam DataFrame
    if target_column not in df.columns or not set(feature_columns).issubset(df.columns):
        raise ValueError("Kolom target atau fitur tidak ditemukan di DataFrame.")

    X = df[feature_columns]  # Fitur
    y = df[target_column]    # Target
    return X, y

def train_model():
    datasets = [
        "dataset-prediksi-sem2.csv",
        "dataset-prediksi-sem3.csv",
        "dataset-prediksi-sem4.csv",
        "dataset-prediksi-sem5.csv",
        "dataset-prediksi-sem6.csv",
        "dataset-prediksi-sem7.csv"
    ]

    # Inisialisasi model Linear Regression
    model = LinearRegression()

    for dataset in datasets:
        # Membaca dataset
        target_column = 'ips-next'
        X, y = read_data(dataset, target_column=target_column, feature_columns=['ips-now'])

        print(f"\nTraining Linear Regression Model using {dataset}")

        # Membagi data menjadi data latih, data validasi, dan data uji
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

        # Latih model
        model.fit(X_train, y_train)

        # Prediksi pada data validasi
        y_val_pred = model.predict(X_val)

        # Evaluasi pada data validasi
        mse_val = mean_squared_error(y_val, y_val_pred)
        r2_val = r2_score(y_val, y_val_pred)

        # Prediksi pada data uji
        y_test_pred = model.predict(X_test)

        # Evaluasi pada data uji
        mse_test = mean_squared_error(y_test, y_test_pred)
        r2_test = r2_score(y_test, y_test_pred)

        # Menampilkan hasil evaluasi
        print(f"MSE (Validation): {mse_val}")
        print(f"R-squared (Validation): {r2_val}")
        print(f"MSE (Test): {mse_test}")
        print(f"R-squared (Test): {r2_test}")

        # Plot hasil prediksi pada data validasi dan data uji
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.scatter(y_val, y_val_pred)
        plt.title(f"Linear Regression - {dataset} - Validation Set")
        plt.xlabel("True Values")
        plt.ylabel("Predictions")

        plt.subplot(1, 2, 2)
        plt.scatter(y_test, y_test_pred)
        plt.title(f"Linear Regression - {dataset} - Test Set")
        plt.xlabel("True Values")
        plt.ylabel("Predictions")

        plt.tight_layout()
        plt.show()

    # Setelah semua pelatihan selesai, simpan model secara keseluruhan
    model_save_path = "linear_regression_model.joblib"
    joblib.dump(model, model_save_path)

if __name__ == "__main__":
    train_model()