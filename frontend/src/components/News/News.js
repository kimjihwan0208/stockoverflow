import React from 'react';
import './News.css';
import Article from './Article/Article';
import { newsData } from '../../mocks/newsData';

function News(props) {
  const { articles } = props;

  return (
    <div className="news__container">
      <div className="row">
        {articles && articles.map(article => {
          return (
            <div className="col-4">
              <Article {...article} />
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default News;