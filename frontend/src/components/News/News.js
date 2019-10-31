import React from 'react';
import './News.css';
import Article from './Article/Article';
import { newsData } from '../../mocks/newsData';

function News() {
  return (
    <div className="news__container">
      <div className="row justify-content-center">
        {newsData && newsData.map(article => {
          return (
            <div className="col-3">
              <Article {...article} />
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default News;