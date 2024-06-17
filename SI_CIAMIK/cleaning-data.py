import pandas as pd

# Membaca file CSV
df = pd.read_csv('data-ips-poltekssn.csv', sep=';')

# Mendefinisikan fungsi untuk mengubah nilai IPS dari string ke float
def convert_ips_to_float(ips_str):
    if pd.isnull(ips_str):  # Memeriksa jika nilai adalah NaN
        return ips_str
    else:
        return float(ips_str.replace(',', '.'))  # Mengubah koma menjadi titik dan mengonversi ke float

# Mengubah nilai IPS di setiap kolom '1' hingga '8' menjadi float
for col in ['1', '2', '3', '4', '5', '6', '7', '8']:
    df[col] = df[col].apply(convert_ips_to_float)

df.to_csv('data-ips-poltekssn-cleaned.csv', index=False)