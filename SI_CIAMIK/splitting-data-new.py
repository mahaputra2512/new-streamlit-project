import pandas as pd

# Membaca file CSV
data = pd.read_csv('data-ips-ipk-real.csv')

# Memisahkan tiap kolom menjadi file baru
for kolom in data.columns:
    nama_file = f'{kolom}.csv'
    data[kolom].to_csv(nama_file, index=False)

print("Pemisahan kolom menjadi file baru selesai.")