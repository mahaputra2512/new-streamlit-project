import React from 'react';
import { Bar } from 'react-chartjs-2';

const Graph = ({ data, semester }) => {
  if (!data || !data.length) return null; // Tambahkan kondisi untuk menangani kasus data belum dimuat

  const graphData = {
    labels: data.map((item) => item.nama),
    datasets: [
      {
        label: `IPS Semester ${semester}`,
        data: data.map((item) => item[semester]),
        backgroundColor: 'rgba(75,192,192,0.2)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 1,
      },
    ],
  };

  const options = {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  return (
    <div>
      <h3>Grafik Indeks Prestasi Semester (IPS)</h3>
      <Bar data={graphData} options={options} />
    </div>
  );
};

export default Graph;
