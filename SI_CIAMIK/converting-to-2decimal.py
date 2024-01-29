import pandas as pd

# Membaca file CSV
file_path = "dataset-train-val-test.csv"
df = pd.read_csv(file_path)

# Mengubah nilai desimal menjadi dua angka dibelakang koma
df = df.round(2)

# Menyimpan perubahan kembali ke file CSV
df.to_csv("dataset-train-val-test.csv", index=False)