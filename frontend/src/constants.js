export const BASE_URL = "http://fa8f6936.ngrok.io";

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

export const chooseSentimentTagColor = label => {
  if (label === "positive") {
    return "green";
  } else if (label === "negative") {
    return "red";
  }

  return "gold";
}