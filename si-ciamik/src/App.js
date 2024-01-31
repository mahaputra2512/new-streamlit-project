import React, {useState} from "react";
import Graph from "./components/Graph";
import TopThreeTable from "./components/TopThreeTable";
import Predictions from "./components/Predictions";
import Dropdown from "./components/Dropdown";

function App() {
  // State untuk menyimpan kelas dan semester yang dipilih
  const [selectedClass, setSelectedClass] = useState("4RKSBLUE");
  const [selectedSemester, setSelectedSemester] = useState(1);

  // Mendapatkan data dari backend (misalnya, Flask API)
  const fetchData = async () => {
    // Implementasikan sesuai kebutuhan Anda
    // Gunakan fetch atau library Axios untuk mengambil data dari backend
    // Contoh menggunakan fetch:
    try {
      const response = await fetch(`backend-api-url?kelas=${selectedClass}&semester=${selectedSemester}`);
      const data = await response.json();

      // Lakukan sesuatu dengan data (misalnya, simpan di state)
      // Implementasikan sesuai kebutuhan Anda
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Handle saat tombol "Prediksi Si Ciamik" ditekan
  const handlePredictionButtonClick = async () => {
    // Lakukan prediksi menggunakan backend (misalnya, Flask API)
    // Implementasikan sesuai kebutuhan Anda
    // Pastikan untuk menyertakan kelas, semester, dan data yang diperlukan dalam request ke backend
    try {
      const predictionResponse = await fetch(`backend-prediction-api-url`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          kelas: selectedClass,
          semester: selectedSemester,
          // Tambahkan data lain yang diperlukan untuk prediksi
        }),
      });

      const predictionData = await predictionResponse.json();

      // Lakukan sesuatu dengan hasil prediksi (misalnya, simpan di state atau komponen lain)
      // Implementasikan sesuai kebutuhan Anda
    } catch (error) {
      console.error("Error fetching prediction data:", error);
    }
  };

  return (
    <div>
      <h1>Aplikasi Monitoring IPK dan Mentoring Akademik</h1>

      {/* Dropdown untuk memilih kelas */}
      <Dropdown
        label="Pilih Kelas"
        options={[
          "4RKSBLUE", "4RKSRED", "4RPK", "4RPLK", "4RSK",
          "3RKSECHO", "3RKSROUTE", "3RKSTRACE", "3RPK", "3RPLK", "3RSK",
          "2RKSA", "2RKSB", "2RPK", "2RPLK", "2RSKA", "2RSKB",
          "1RKSA", "1RKSB", "1RKSC", "1RPK", "1RPLK", "1RSK"
        ]}
        selectedValue={selectedClass}
        onSelect={setSelectedClass}
      />

      {/* Dropdown untuk memilih semester */}
      <Dropdown
        label="Pilih Semester"
        options={[1, 2, 3, 4, 5, 6, 7]}
        selectedValue={selectedSemester}
        onSelect={setSelectedSemester}
      />

      {/* Button untuk memuat data */}
      <button onClick={fetchData}>Muat Data</button>

      {/* Komponen Graph */}
      <Graph />

      {/* Komponen TopThreeTable */}
      <TopThreeTable />

      {/* Button untuk prediksi */}
      {selectedSemester < 7 && (
        <button onClick={handlePredictionButtonClick}>Prediksi Si Ciamik</button>
      )}

      {/* Komponen Predictions */}
      <Predictions />
    </div>
  );
};

export default App;