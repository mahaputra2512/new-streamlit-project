import React from "react";

const Predictions = ({handlePrediction}) => {
  return (
    <div>
      <h3>Prediksi Si Ciamik</h3>
      <button onClick={handlePrediction}>Prediksi</button>
    </div>
  );
};

export default Predictions;
