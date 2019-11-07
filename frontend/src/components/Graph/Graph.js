import React from 'react';
import { Line } from 'react-chartjs-2';
import { setOptions } from '../../constants';
import './Graph.css';

function Graph(props) {
  const { dataPoints } = props;

  return (
    <div className="graph__container">
      <div className="graph__innerContainer">
        <Line
          data={
            {
              datasets: [{
                label: "price",
                data: dataPoints,
                backgroundColor:'#F4F8FE',
                borderColor: '#4963EF',
                pointRadius: 5,
                pointHoverRadius: 6,
              }]
            }
          }
          options={setOptions}
        />
      </div>
    </div>
  );
}

export default Graph;
