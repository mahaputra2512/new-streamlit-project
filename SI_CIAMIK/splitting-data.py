import pandas as pd

# Membaca dataset-train-val-test.csv
file_path = 'data-ips-ipk-real.csv'
df = pd.read_csv(file_path)
df = df.drop(['tepat'], axis=1)

# Fungsi untuk membuat dataset baru
def create_new_dataset(df, semester, target_column):
    new_dataset = df[[str(semester), target_column]].copy()
    new_dataset.to_csv(f'dataset-real-prediksi-sem{semester+1}.csv', index=False)

# Membuat dataset baru untuk setiap semester
for semester in range(1, 4):
    target_column = str(semester + 1) if semester < 5 else 'will-dropped'
    create_new_dataset(df, semester, target_column)