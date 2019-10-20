import React from 'react';
import { Line } from 'react-chartjs-2';
import './Graph.css';

const datasets = {
  datasets: [{
    label: "test",
    data: [
    {
      t: "6:30",
      y: 12
    },
    {
      t: "7:30",
      y: 13
    },
    {
      t: "8:30",
      y: 24
    },
    {
      t: "9:30",
      y: 1
    }
  ],
  backgroundColor:'#F4F8FE',
  borderColor: '#4963EF',
  pointRadius: 5,
  pointHoverRadius: 6,
  }]
}

const setOptions = {
  responsive: true,
  scales: {
    xAxes: [{
      offset: true,
      type: 'time',
      gridLines: {
        display: false
      },
      time:
        {
          stepSize: 1,
          unit: 'hour',
          format: 'HH:mm',
          parser: 'HH:mm',
          min: '6:30',
          max: '13:00',
          displayFormats: { hour: 'HH:mm' }
        }
    }],
    yAxes: [{
      ticks: {
        beginAtZero: true
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
    display: false,
  }
}

function Graph() {
  return (
    <div className="graph__container">
      <div className="graph__innerContainer">
        <Line
          data={datasets}
          options={setOptions}
        />
      </div>
    </div>
  );
}

export default Graph;
