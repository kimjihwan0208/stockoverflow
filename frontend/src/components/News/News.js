import React from 'react';
import './News.css';
import Article from './Article/Article';

function News() {
  return (
    <div className="news__container">
      <div className="row justify-content-center">
        <div className="col-3">
          <Article />
        </div>
        <div className="col-3">
          <Article />
        </div>
        <div className="col-3">
          <Article />
        </div>
        <div className="col-3">
          <Article />
        </div>
      </div>
    </div>
  )
}

export default News;