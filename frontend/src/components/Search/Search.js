import React, { useState, useEffect } from 'react';
import './Search.css';
import { Form, Button, Icon, DatePicker, Select } from 'antd';
import { BASE_URL, showMessage, defaultDate, SEARCH_ERROR } from '../../constants';
const moment = require('moment');

const { Item } = Form;
const { Option } = Select;

function Search(props) {
  const { handleSearchResponse } = props;
  const [date, setDate] = useState('');
  const [selectDefaultValue, setSelectDefaultValue] = useState('Select a stock symbol');
  const [isLoading, setIsLoading] = useState(false);
  const [isSelectLoading, setIsSelectLoading] = useState(false);
  const [stockSymbols, setStockSymbols] = useState([]);
  const [selectedValue, setSelectedValue] = useState('');

  useEffect(() => {
    setDate(defaultDate);
    handleDateChange(defaultDate, defaultDate);
  }, []);

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
      console.log(resp)
      const { Stocks, Terms, Articles, Open, Close } = resp;
      const list = Stocks.map(item => ({ "t": item.time, "y": item.Value }));
      handleSearchResponse(list, Terms, Articles, Open, Close);
      setIsLoading(false);
    })
    .catch(err => {
      console.error(err);
      setIsLoading(false);
      showMessage(SEARCH_ERROR);
    });
  }

  const handleDateChange = (date, dateString) => {
    setIsSelectLoading(true);

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
        setIsSelectLoading(false);
      })
      .catch(err => {
        setIsSelectLoading(false);
        console.error(err);
        showMessage(SEARCH_ERROR);
      });

    setDate(dateString);
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
                defaultValue={moment("11/13/2006")}
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
