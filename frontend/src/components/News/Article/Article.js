import React, { useState } from 'react';
import './Article.css';
import { Modal, Tag } from 'antd';
import Dotdotdot from 'react-dotdotdot';
import { chooseSentimentTagColor } from '../../../constants';

function Article(props) {
  const [isArticleOpen, setIsArticleOpen] = useState(false);

  const handleArticleClick = () => {
    setIsArticleOpen(true);
  }

  const handleArticleClose = () => {
    setIsArticleOpen(false);
  }

  return (
    <div className="article__container">
      <div className="article__wrapper" onClick={handleArticleClick}>
        <div className="row justify-content-center">
          <div className="col-10">
            <div className="article__title--container"> 
              <Dotdotdot clamp={2} className="article__title">
                {props.title}
              </Dotdotdot>
            </div>
          </div>
        </div>
        <div className="row justify-content-center article__secondRow">
          <div className="col-8">
            <div className="article__timestamp"><em>{props.timestamp}</em></div>
          </div>
          <div className="col-2">
            <Tag className="article__sentiment" color={chooseSentimentTagColor(props.label)}>{props.label}</Tag>
          </div>
        </div>
      </div>
      <Modal
        centered
        visible={isArticleOpen}
        onCancel={handleArticleClose}
        footer={null}
        width={600}
      >
        <div className="article__modal--container">
          <div className="article__modal--title">{props.title}</div>
          <div className="article__modal--timestamp"><em>{props.timestamp}</em></div>
          <Tag className="article__modal--sentiment" color={chooseSentimentTagColor(props.label)}>{props.label}</Tag>
          <div className="article__modal--description">{props.description}</div>
        </div>
      </Modal>
    </div>
  );
}

export default Article;