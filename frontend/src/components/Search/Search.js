import React, { useState, useEffect } from 'react';
import './Search.css';
import { Form, Input, Button, Icon, DatePicker, Select } from 'antd';
import { stockSymbols as mockStockSymbols } from '../../mocks/stockSymbols';
import { BASE_URL } from '../../constants';

const { Item } = Form;
const { Option } = Select;

function Search(props) {
  const [date, setDate] = useState('');
  const [selectDefaultValue, setSelectDefaultValue] = useState('Select a stock symbol');
  const [isLoading, setIsLoading] = useState(false);
  const [isSelectLoading, setIsSelectLoading] = useState(false);
  const [stockSymbols, setStockSymbols] = useState([]);
  const [selectedValue, setSelectedValue] = useState('');


  const handleSubmit = e => {
    e.preventDefault();

    setIsLoading(true);
    fetch(`${BASE_URL}/api/stockdata`,{
      headers: {
        'Content-Type': 'application/json'
      },
      method: "POST",
      body: JSON.stringify({
        "date": date,
        "stock": selectedValue
      }),
    })
    .then(resp => resp.json())
    .then(resp => {

      let temp = {}
      let dataSets = [];
      let labels = [];
      let dataset1 = {};
      let dataset2 = {};
      let stocksList = resp.Stocks;
      let temp1 = [];
      let temp2 = [];

      for (let i = 0; i < stocksList.length; ++i){
        labels.push(stocksList[i].time);
        temp1.push(stocksList[i].Value);
        temp2.push(resp.Open)
      }

      dataset1 = {
        label: "date",
        data: temp1,
        borderColor:'rgba(63, 63, 191, 0.6)',
        fill: false
      }

      dataset2 = {
        label: "Current Date",
        data: temp2,
        borderColor:'rgba(255, 35, 35, 0.6)',
        fill: false
      }

      dataSets.push(dataset1);
      dataSets.push(dataset2);
      temp = {
        labels: labels,
        datasets: dataSets
      }
      props.handleSearch(temp)
      setIsLoading(false);
    })
    .catch(err => console.log(err))

  }

  const handleDateChange = (date, dateString) => {
    console.log(dateString)

    fetch(`${BASE_URL}/api/date-to-stocks`, {
        headers: {
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({
          "date": dateString
        }),
      })
      .then(resp => resp.json())
      .then(resp => {
        setStockSymbols(resp.Stocks);
        setSelectDefaultValue(stockSymbols[0]);
      })
      .catch(err => console.log(err))

    setDate(dateString)

    // TODO: Fetch all the stock symbols for the selected date from the backend
    // Use setStockSymbols to update the stockSymbols array
    // setTimeout(() => {
    //   setStockSymbols(mockStockSymbols);
    //   setSelectDefaultValue(stockSymbols[0]);
    //   setIsSelectLoading(false);
    // }, 3000);
  }

  const handleStockChange = (value) => {
    setSelectedValue(value);
  }

  return (
    <div className="search__container">
      <div className="container-fluid">
        <div className="row justify-content-center">
          <Form layout="inline" onSubmit={handleSubmit}>
            <Item>
              <DatePicker
                onChange={handleDateChange}
                format="MM/DD/YYYY"
                style={{ width: 200 }}
              />
            </Item>
            <Item>
              <Select
                prefix={<Icon type="search" style={{ color: 'rgba(0,0,0,.25)' }} />}
                className="search__stock"
                name="stockSymbol"
                defaultValue={selectDefaultValue}
                style={{ width: 250 }}
                disabled={!stockSymbols.length}
                loading={isSelectLoading}
                onChange={handleStockChange}
              >
                {stockSymbols.length > 0 && stockSymbols.map(stockSymbol => {
                  return <Option value={stockSymbol}>{stockSymbol}</Option>
                })}
              </Select>
            </Item>
            <Item>
              <Button
                className="search__submit"
                type="primary"
                htmlType="submit"
                loading={isLoading}
              >
                SEARCH
              </Button>
            </Item>
          </Form>
        </div>
      </div>
    </div>
  );
}

export default Search;
