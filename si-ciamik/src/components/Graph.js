import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';

const Graph = ({ data, semester }) => {
  const [chartData, setChartData] = useState({});
  console.log(data);

  useEffect(() => {
    if (data && data.length) {
        console.log(data);
        const labels = data.map((item) => item.nama);

        setChartData({
            labels: labels,
            datasets: [
            {
                label: `IPS Semester ${semester}`,
                data: data.map((item) => item[semester]),
                backgroundColor: 'rgba(75,192,192,0.2)',
                borderColor: 'rgba(75,192,192,1)',
                borderWidth: 1,
            },
            ],
        });
        }
    }, [data, semester]);

  return (
    <div>
      <h3>Grafik Indeks Prestasi Semester (IPS)</h3>
      <Bar data={chartData} />
    </div>
  );
};

export default Graph;
