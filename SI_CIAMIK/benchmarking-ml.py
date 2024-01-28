import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Fungsi untuk membaca data dari file CSV dan membagi menjadi fitur dan target
def read_data(file_path):
    df = pd.read_csv(file_path)
    X = df.drop(columns=['nama', '2', '3', '4', '5', '6', '7'])  # Fitur
    y = df['2']  # Target, kita akan memprediksi nilai pada semester 2
    return X, y

# Fungsi untuk melatih dan mengevaluasi model
def train_and_evaluate_model(model, X_train, y_train, X_val, y_val, X_test, y_test):
    # Latih model
    model.fit(X_train, y_train)

    # Prediksi pada data validasi
    y_val_pred = model.predict(X_val)

    # Evaluasi pada data validasi
    accuracy_val = accuracy_score(y_val, y_val_pred)
    precision_val = precision_score(y_val, y_val_pred, average='weighted')
    recall_val = recall_score(y_val, y_val_pred, average='weighted')

    # Prediksi pada data uji
    y_test_pred = model.predict(X_test)

    # Evaluasi pada data uji
    accuracy_test = accuracy_score(y_test, y_test_pred)
    precision_test = precision_score(y_test, y_test_pred, average='weighted')
    recall_test = recall_score(y_test, y_test_pred, average='weighted')

    return {
        'Accuracy (Validation)': accuracy_val,
        'Precision (Validation)': precision_val,
        'Recall (Validation)': recall_val,
        'Accuracy (Test)': accuracy_test,
        'Precision (Test)': precision_test,
        'Recall (Test)': recall_test,
    }

# Fungsi untuk membaca dataset dan melakukan pembelajaran
def main():
    # Nama file dataset
    datasets = ["dummy-ml-semester2.csv", "dummy-ml-semester3.csv", "dummy-ml-semester4.csv",
                "dummy-ml-semester5.csv", "dummy-ml-semester6.csv", "dummy-ml-semester7.csv"]

    for dataset in datasets:
        print(f"\nDataset: {dataset}")

        # Membaca dataset
        X, y = read_data(dataset)

        # Membagi data menjadi data latih, data validasi, dan data uji
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

        # Inisialisasi model
        models = {
            'Linear Regression': LinearRegression(),
            'Random Forest': RandomForestRegressor(),
            'XGBoost': XGBRegressor(),
            'LightGBM': LGBMRegressor(),
            'CatBoost': CatBoostRegressor(silent=True),
        }

        # Melatih dan mengevaluasi setiap model
        for model_name, model in models.items():
            print(f"\nModel: {model_name}")
            results = train_and_evaluate_model(model, X_train, y_train, X_val, y_val, X_test, y_test)

            # Menampilkan hasil evaluasi
            for metric, value in results.items():
                print(f"{metric}: {value}")

if __name__ == "__main__":
    main()