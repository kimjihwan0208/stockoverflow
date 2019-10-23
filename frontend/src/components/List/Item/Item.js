import React from 'react';
import './Item.css';
import { Tooltip } from 'antd';

function Item(props) {
  const adjustedBackgroundColor = `rgba(73, 99, 239, ${1 - ((props.index + 1) * 0.1)})`;

  return (
    <div className="item__container" style={{ backgroundColor: adjustedBackgroundColor }}>
      <Tooltip title={props.score}>
        <div className="item__value">{props.value}</div>
      </Tooltip>
    </div>
  );
}

export default Item;