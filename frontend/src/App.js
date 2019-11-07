import React, { useState } from 'react';
import './App.css';
import Search from './components/Search/Search';
import Graph from './components/Graph/Graph';
import List from './components/List/List';
import News from './components/News/News';
import logo from './assets/logo.svg';
import {Animated} from "react-animated-css";

function App() {
  const [dataPoints, setDataPoints] = useState([]);
  const [terms, setTerms] = useState([]);
  const [articles, setArticles] = useState([]);
  const [openingStock, setOpeningStock] = useState(null);
  const [closingStock, setClosingStock] = useState(null);

  const handleSearchResponse = (dataPoints, terms, articles, openingStock, closingStock) => {
    console.log("got terms")
    setDataPoints(dataPoints);
    setTerms(terms);
    setArticles(articles);
    setOpeningStock(openingStock);
    setClosingStock(closingStock);
  }

  return (
  <Animated animationIn="fadeIn">
    <div className="App">
      <div className="container-fluid">
        <div className="row justify-content-center">
          <img src={logo} alt="" className="App__logo"/>
          <Search handleSearchResponse={handleSearchResponse}/>
        </div>
        <div className="row justify-content-center">
          <div className="col-8">
            <div className="App__stockTitle--container">
              <h1 className="App__stockTitle">Stock Graph</h1>
            </div>
            <Graph dataPoints={dataPoints} openingStock={openingStock} closingStock={closingStock} />
          </div>
          <div className="col-3">
            <div className="App__listTitle--container">
              <h1 className="App__listTitle">Impactful Terms</h1>
            </div>
            <List terms={terms} />
          </div>
        </div>
        <div className="row justify-content-center">
          <div className="col-11">
            <div className="App__newsTitle--container">
              <h1 className="App__newsTitle">Relevant News</h1>
            </div>
            <News articles={articles} />
          </div>
        </div>
      </div>
    </div>
  </Animated>
  );
}

export default App;
