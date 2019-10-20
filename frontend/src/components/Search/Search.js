import React, { useState } from 'react';
import './Search.css';
import { Form, Input, Button, Icon, DatePicker } from 'antd';

const { Item } = Form;

function Search() {
  const [date, setDate] = useState('');

  const handleSubmit = e => {
    e.preventDefault();

    console.log("Got stock symbol", e.target.stockSymbol.value)
  }

  const handleDateChange = (date, dateString) => {
    console.log("Got date and dateString", date, dateString);

    setDate(dateString)
  }

  return (
    <div className="search__container">
      <div className="container-fluid">
        <div className="row justify-content-center">
          <Form layout="inline" onSubmit={handleSubmit}>
            <Item>
              <Input
                prefix={<Icon type="search" style={{ color: 'rgba(0,0,0,.25)' }} />}
                className="search__stock"
                name="stockSymbol"
                placeholder="Input stock symbol"
                style={{ width: 250 }}
              />
            </Item>
            <Item>
              <DatePicker
                onChange={handleDateChange}
                format="MM/DD/YYYY"
                style={{ width: 250 }}
              />
            </Item>
            <Item>
              <Button
                className="search__submit"
                type="primary"
                htmlType="submit"
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