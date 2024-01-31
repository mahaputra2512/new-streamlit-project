import React, { useState, useEffect } from "react";
import Graph from "./components/Graph";
import TopThreeTable from "./components/TopThreeTable";
import Predictions from "./components/Predictions";
import Dropdown from "./components/Dropdown";

function App() {
  const [selectedClass, setSelectedClass] = useState("4RKSBLUE");
  const [selectedSemester, setSelectedSemester] = useState(1);
  const [data, setData] = useState({}); // State untuk menyimpan data

  useEffect(() => {
    fetchData(); // Panggil fetchData saat komponen pertama kali di-mount
    setData(fetchData);
  }, []); // [] sebagai dependencies agar useEffect hanya dijalankan sekali

  useEffect(() => {
    // Ini akan dijalankan setiap kali nilai data berubah
    console.log("Data Updated:", data);
  }, [data]);

  const fetchData = async () => {
    try {
      const response = await fetch(`http://localhost:5000/fetch_data`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          kelas: selectedClass,
          semester: selectedSemester,
        }),
      });
      const fetchedData = await response.json();
      console.log(fetchedData); 
      return fetchedData;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handlePredictionButtonClick = async () => {
    try {
      const predictionResponse = await fetch(`http://localhost:5000/predict`, {
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
      // Lakukan sesuatu dengan hasil prediksi (misalnya, simpan di state)
      // Implementasikan sesuai kebutuhan Anda
      console.log("Prediction Data:", predictionData);
    } catch (error) {
      console.error("Error fetching prediction data:", error);
    }
  };

  return (
    <div>
      <h1>Aplikasi Monitoring IPK dan Mentoring Akademik</h1>

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

      <Dropdown
        label="Pilih Semester"
        options={[1, 2, 3, 4, 5, 6, 7]}
        selectedValue={selectedSemester}
        onSelect={setSelectedSemester}
      />

      <button onClick={fetchData}>Muat Data</button>

      <Graph data={data} semester={selectedSemester} />

      <TopThreeTable data={data} semester={selectedSemester} />

      {selectedSemester < 7 && (
        <Predictions handlePrediction={handlePredictionButtonClick} />
      )}
    </div>
  );
}

export default App;