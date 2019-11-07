import React from 'react';
import { Line } from 'react-chartjs-2';
import { setOptions } from '../../constants';
import './Graph.css';

function Graph(props) {
  const { dataPoints, openingStock, closingStock } = props;

  const convert = () => {
    const currentPrice = dataPoints.map(dataPoint => dataPoint.y);
    const opening = dataPoints.map(() => openingStock);
    const closing = dataPoints.map(() => closingStock);
    const time = dataPoints.map(dataPoint => dataPoint.t);

    const dataSet = {
      labels: time,
      datasets: [{
        label: "Current Price",
        data: currentPrice,
        backgroundColor:'#F4F8FE',
        borderColor: '#4963EF',
      },
      {
        label: "Opening",
        fill: false,
        data: opening,
        backgroundColor: 'rgba(255, 35, 35, 0.6)'
      },
      {
        label: "Closing",
        fill: false,
        data: closing,
        backgroundColor: 'rgba(255, 35, 35, 0.6)'
      }
      ]
    }

    return dataSet
  }

  return (
    <div className="graph__container">
      <div className="graph__innerContainer">
        <Line
          data={convert}
          options={setOptions}
        />
      </div>
    </div>
  );
}

export default Graph;
