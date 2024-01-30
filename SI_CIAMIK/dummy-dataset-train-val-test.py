import pandas as pd
import random

# Fungsi untuk membuat dataset dummy
def create_dummy_dataset(num_samples=100):
    # Generate random names for taruna
    taruna_names = [f"Taruna-{i}" for i in range(1, num_samples + 1)]

    # Inisialisasi kolom-kolom dataset
    dataset = pd.DataFrame({
        'nama': taruna_names,
        '1': [random.uniform(3.7, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 1
        '2': [random.uniform(3.5, 3.7) for _ in range(num_samples)],  # Nilai IPS Semester 2
        '3': [random.uniform(3.75, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 3
        '4': [random.uniform(3.8, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 4
        '5': [random.uniform(3.85, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 5
        '6': [random.uniform(3.9, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 6
        '7': [random.uniform(3.95, 4.0) for _ in range(num_samples)],  # Nilai IPS Semester 7
    })

    # Hitung nilai IPK (rata-rata dari Semester 1-7)
    dataset['ipk'] = dataset[['1', '2', '3', '4', '5', '6', '7']].mean(axis=1)

    # Membuat penurunan nilai maksimal 2 kali dengan maksimal penurunan 0.5
    for _ in range(2):
        taruna_index = random.randint(0, num_samples - 1)
        semester_to_drop = random.randint(1, 7)
        max_drop = min(0.5, dataset.at[taruna_index, str(semester_to_drop)])

        # Mengurangkan nilai pada semester yang dipilih
        dataset.at[taruna_index, str(semester_to_drop)] -= random.uniform(0.1, max_drop)

    return dataset

# Membuat dataset dummy dengan 150 sampel
dummy_dataset = create_dummy_dataset(num_samples=100000)

# Menyimpan dataset ke file CSV
dummy_dataset.to_csv('dataset-train-val-test.csv', index=False)

print("Dataset berhasil dibuat dan disimpan.")