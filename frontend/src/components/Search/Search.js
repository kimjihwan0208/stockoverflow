import React, { useState, useEffect } from 'react';
import './Search.css';
import { Form, Input, Button, Icon, DatePicker, Select } from 'antd';
import { stockSymbols as mockStockSymbols } from '../../mocks/stockSymbols';

const { Item } = Form;
const { Option } = Select;

function Search() {
  const [date, setDate] = useState('');
  const [selectDefaultValue, setSelectDefaultValue] = useState('Select a stock symbol');
  const [isLoading, setIsLoading] = useState(false);
  const [isSelectLoading, setIsSelectLoading] = useState(false);
  const [stockSymbols, setStockSymbols] = useState([]);

  const handleSubmit = e => {
    e.preventDefault();

    setIsLoading(true);
    setTimeout(() => setIsLoading(false), 3000);

    console.log("Got stock symbol", e.target.stockSymbol.value)
  }

  const handleDateChange = (date, dateString) => {
    console.log("Got date and dateString", date, dateString);

    setDate(dateString)
    setIsSelectLoading(true)

    // TODO: Fetch all the stock symbols for the selected date from the backend
    // Use setStockSymbols to update the stockSymbols array
    setTimeout(() => {
      setStockSymbols(mockStockSymbols);
      setSelectDefaultValue(stockSymbols[0]);
      setIsSelectLoading(false);
    }, 3000);
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