import pandas as pd
import numpy as np

# Fungsi untuk membuat dataset dummy dan menyimpannya ke file CSV
def create_dummy_dataset(filename, num_semesters, num_students=1000):
    # Generate data
    np.random.seed(42)  # Untuk hasil yang dapat direproduksi
    students = [f"Taruna-{i}" for i in range(1, num_students + 1)]

    data = {
        "nama": students,
    }

    for semester in range(1, num_semesters + 1):
        ips_values = np.random.uniform(2.0, 4.0, num_students)  # Nilai IPS antara 2.0 dan 4.0
        data[str(semester)] = ips_values

    # Membuat DataFrame
    df = pd.DataFrame(data)

    # Simpan ke file CSV
    df.to_csv(filename, index=False)
    print(f"Dataset {filename} berhasil dibuat dengan {num_students} data.")

# Membuat dataset untuk masing-masing semester
create_dummy_dataset("dummy-ml-semester2.csv", num_semesters=2, num_students=1000)
create_dummy_dataset("dummy-ml-semester3.csv", num_semesters=3, num_students=1000)
create_dummy_dataset("dummy-ml-semester4.csv", num_semesters=4, num_students=1000)
create_dummy_dataset("dummy-ml-semester5.csv", num_semesters=5, num_students=1000)
create_dummy_dataset("dummy-ml-semester6.csv", num_semesters=6, num_students=1000)
create_dummy_dataset("dummy-ml-semester7.csv", num_semesters=7, num_students=1000)
