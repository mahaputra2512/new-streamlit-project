import pandas as pd

# Membaca dataset-train-val-test.csv
file_path = 'data-ips-ipk-real.csv'
df = pd.read_csv(file_path)
df = df.drop(['tepat'], axis=1)
# Menyimpan DataFrame ke dalam file CSV
df.to_csv('data-ips-ipk-real.csv', index=False)  # index=False agar indeks tidak disimpan dalam file CSV