import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import './Graph.css';


const setOptions = {
  responsive: true,
  scales: {
    xAxes: [{
      offset: true,
      type: 'time',
      gridLines: {
        display: false
      },
      ticks: {
        fontFamily: "'Ubuntu', sans-serif"
      },
      time:
        {
          stepSize: 1,
          unit: 'hour',
          format: 'HH:mm',
          parser: 'HH:mm',
          min: '9:30',
          max: '15:30',
          displayFormats: { hour: 'HH:mm' }
        }
    }],
    yAxes: [{
      ticks: {
        fontFamily: "'Ubuntu', sans-serif"
      },
      gridLines: {
        display: false
      }
    }]
  },
  maintainAspectRatio: false,
  title:{
    display: false
  },
  legend:{
    labels: {
      defaultFontFamily: "'Ubuntu', sans-serif"
    },
    display: false,
  }
}

function Graph(props) {
  const [graphPoints, setGraphPoints] = useState([])

  console.log(props.dataPoints)
  return (
    <div className="graph__container">
      <div className="graph__innerContainer">
        <Line
          data={props.dataPoints}
          options={setOptions}
        />
      </div>
    </div>
  );
}

export default Graph;
