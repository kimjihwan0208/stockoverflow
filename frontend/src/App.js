import React from 'react';
import './App.css';
import Search from './components/Search/Search';
import Graph from './components/Graph/Graph';
import List from './components/List/List';
import News from './components/News/News';

function App() {
  return (
    <div className="App">
      <div className="container-fluid">
        <div className="row justify-content-center">
          <Search />
        </div>
        <div className="row justify-content-center">
          <div className="col-8">
            <div className="App__stockTitle--container">
              <h1 className="App__stockTitle">Stock Graph</h1>
            </div>
            <Graph />
          </div>
          <div className="col-3">
            <div className="App__listTitle--container">
              <h1 className="App__listTitle">Impactful Terms</h1>
            </div>
            <List />
          </div>
        </div>
        <div className="row justify-content-center">
          <div className="col-11">
            <div className="App__newsTitle--container">
              <h1 className="App__newsTitle">Relevant News</h1>
            </div>
            <News />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
