import React from 'react';
import './Article.css';

function Article(props) {
  return (
    <div className="article__container">
      <div className="row justify-content-center">
        <div className="col-8">
          <div className="article__title">{props.title}</div>
        </div>
        <div className="col-2">
          <div className="article__sentiment">{props.sentiment}</div>
        </div>
      </div>
      <div className="row justify-content-center">
        <div className="article__description">{props.description}</div>
      </div>
    </div>
  );
}

export default Article;