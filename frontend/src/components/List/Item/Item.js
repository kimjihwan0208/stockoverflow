import React from 'react';
import './Item.css';
import { Tooltip } from 'antd';

function Item(props) {
  console.log(props)
  const { index, score, value } = props;
  const adjustedBackgroundColor = `rgba(73, 99, 239, ${1 - ((index + 1) * 0.1)})`;

  console.log("got a score", score);

  return (
    <div className="item__container" style={{ backgroundColor: adjustedBackgroundColor }}>
      <Tooltip title={score}>
        <div className="item__value">{value}</div>
      </Tooltip>
    </div>
  );
}

export default Item;