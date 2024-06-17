import pandas as pd

# Membaca dataset-train-val-test.csv
file_path = 'data-ips-poltekssn-cleaned.csv'
df = pd.read_csv(file_path)

# Fungsi untuk membuat dataset baru
def create_new_dataset(df, semester, target_column):
    new_dataset = df[[str(semester), target_column]].copy()
    new_dataset.to_csv(f'data-ips-poltekssn-sem{semester+1}.csv', index=False)

# Membuat dataset baru untuk setiap semester
for semester in range(1, 8):
    target_column = str(semester + 1) if semester < 8 else 'will-dropped'
    create_new_dataset(df, semester, target_column)