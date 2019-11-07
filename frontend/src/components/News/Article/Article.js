import React, { Fragment, useState } from 'react';
import './Article.css';
import { Modal, Tag } from 'antd';
import Dotdotdot from 'react-dotdotdot';
import { chooseSentimentTagColor } from '../../../constants';

function Article(props) {
  const { title, date, sentiment, summary, terms } = props;
  const [isArticleOpen, setIsArticleOpen] = useState(false);

  const handleArticleClick = () => {
    setIsArticleOpen(true);
  }

  const handleArticleClose = () => {
    setIsArticleOpen(false);
  }

  const formatSummaryWord = (word, terms) => {
    return terms.includes(word) ? 
      <Fragment><span className="article__modal--highlight">{word}</span> </Fragment> :
      word + " ";
  }

  console.log(date)

  return (
    <div className="article__container">
      <div className="article__wrapper">
        <div className="row justify-content-center">
          <div className="col-10">
            <div className="article__title--container" onClick={handleArticleClick}> 
              <Dotdotdot clamp={2} className="article__title">
                {title}
              </Dotdotdot>
            </div>
          </div>
        </div>
        <div className="row justify-content-center article__secondRow">
          <div className="col-8">
            <div className="article__timestamp"><em>{date}</em></div>
          </div>
          <div className="col-2">
            <Tag className="article__sentiment" color={chooseSentimentTagColor(sentiment)}>{sentiment}</Tag>
          </div>
        </div>
      </div>
      <Modal
        centered
        visible={isArticleOpen}
        onCancel={handleArticleClose}
        footer={null}
        width={600}
        className="article__modal"
      >
        <div className="article__modal--container">
          <div className="article__modal--title">{title}</div>
          <div className="article__modal--timestamp"><em>{date}</em></div>
          <Tag className="article__modal--sentiment" color={chooseSentimentTagColor(sentiment)}>{sentiment}</Tag>
          <div className="article__modal--description">
            {summary.split(" ").map(word => formatSummaryWord(word, terms))}
          </div>
        </div>
      </Modal>
    </div>
  );
}

export default Article;