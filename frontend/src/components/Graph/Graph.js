import React from 'react';
import { Line } from 'react-chartjs-2';
import { setOptions } from '../../constants';
import './Graph.css';

// const  dataSet =
// {
//               labels: ["Jun-06", "Jun-07", "Jun-08", "Jun-09", "Jun-10", "Jun-11", "Jun-12", "Jun-13"],
//               datasets: [
//                 {
//                   label:'Device_1',
//                   data:[1, 4, 8, 2, 20, 23, 14, 9],
//                   backgroundColor:'rgba(63, 63, 191, 0.6)'
//                 },
//                 {
//                   label:'Device_2',
//                   data:[23, 17, 30, 5, 3, 2, 13, 15],
//                   backgroundColor: 'rgba(255, 35, 35, 0.6)'
//                 }
//               ]
//         }

// const dataSet = {
//   labels: ["9:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30"]
//   datasets: [
//     label: "current"
//     backgroundColor:'rgba(63, 63, 191, 0.6)'
//   ]
// }

function Graph(props) {
  const { dataPoints, openingStock, closingStock } = props;

    const convert = () => {
      let temp1 = []
      let temp2 = []
      let temp3 = []
      let time = []

      for (let i = 0; i < dataPoints.length; ++i){
        time.push(dataPoints[i].t)
        temp1.push(dataPoints[i].y)
        temp2.push(openingStock)
        temp3.push(closingStock)
      }

      let dataSet = {
        labels: time,
        datasets: [{
          label: "Stock1",
          fill: false,
          data: temp1,
          backgroundColor:'rgba(63, 63, 191, 0.6)'
        },
        {
          label: "Opening",
          fill: false,
          data: temp2,
          backgroundColor: 'rgba(255, 35, 35, 0.6)'
        },
        {
          label: "Closing",
          fill: false,
          data: temp3,
          backgroundColor: 'rgba(255, 35, 35, 0.6)'
        }
        ]
      }

    return dataSet
  }

  console.log(openingStock)
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
