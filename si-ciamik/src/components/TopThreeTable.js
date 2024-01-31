import React from "react";

const TopThreeTable = ({ data, semester }) => {
  if (!data || !data.length) return null; // Tambahkan kondisi untuk menangani kasus data belum dimuat

  const topThree = data.sort((a, b) => b[semester] - a[semester]).slice(0, 3);

  return (
    <div>
      <h3>Peraih Sanapati Cendekia</h3>
      <table>
        <thead>
          <tr>
            <th>Nama</th>
            <th>IPS Semester {semester}</th>
          </tr>
        </thead>
        <tbody>
          {topThree.map((item) => (
            <tr key={item.nama}>
              <td>{item.nama}</td>
              <td>{item[semester]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TopThreeTable;
