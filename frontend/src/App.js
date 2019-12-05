import React, { useState } from 'react';
import './App.css';
import Search from './components/Search/Search';
import Graph from './components/Graph/Graph';
import List from './components/List/List';
import News from './components/News/News';
import logo from './assets/logo.svg';
import { Animated } from "react-animated-css";
import { Modal } from 'antd';
import upArrow from './assets/up-arrow.svg';
import downArrow from './assets/down-arrow.svg';
import Bounce from 'react-reveal/Bounce';

function App() {
  const [dataPoints, setDataPoints] = useState([]);
  const [terms, setTerms] = useState([]);
  const [articles, setArticles] = useState([]);
  const [openingStock, setOpeningStock] = useState(null);
  const [closingStock, setClosingStock] = useState(null);
  const [companyName, setCompanyName] = useState("");
  const [prediction, setPrediction] = useState("");
  const [predictionMessage, setPredictionMessage] = useState("");
  const [stockSymbol, setStockSymbol] = useState("");
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleSearchResponse = data => {
    const { dataPoints, terms, articles, openingStock, closingStock, companyName, prediction, predictionMessage, stockSymbol } = data;
    setDataPoints(dataPoints);
    setTerms(terms);
    setArticles(articles);
    setOpeningStock(openingStock);
    setClosingStock(closingStock);
    setCompanyName(companyName);
    setPrediction(prediction);
    setPredictionMessage(predictionMessage);
    setStockSymbol(stockSymbol);

    if (companyName && prediction && predictionMessage && stockSymbol) {
      setIsModalOpen(true);
    }
  }

  const handleCloseModal = () => setIsModalOpen(false);

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
        <Modal
          visible={isModalOpen}
          onCancel={handleCloseModal}
          footer={null}
          centered
        >
          <Bounce>
            <div className="App__arrow--wrapper">
              <div className="App__stockSymbol">
                {stockSymbol}
                {prediction === "up" ? (
                  <img src={upArrow} alt="" className="App__arrow" />
                ) : (
                  <img src={downArrow} alt="" className="App__arrow" />
                )}
              </div>
            </div>
            <div className="App__companyName">{companyName}</div>
          </Bounce>
          <div className="App__predictionMessage">{predictionMessage}</div>
        </Modal>
      </div>
    </div>
  </Animated>
  );
}

export default App;
