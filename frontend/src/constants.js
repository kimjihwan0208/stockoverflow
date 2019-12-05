import { message } from "antd";

export const BASE_URL = "http://127.0.0.1:5000";
export const defaultDate = "11/13/2006";
export const SEARCH_ERROR = "There was an issue when fetching information for your stock symbol."
export const setOptions = {
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
          stepSize: 0.5,
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

export const chooseSentimentTagColor = label => {
  if (label === "positive") {
    return "green";
  } else if (label === "negative") {
    return "red";
  }

  return "gold";
}

export const showMessage = text => message.error(text);