import React from 'react';
import './Item.css';

function Item(props) {
  const adjustedBackgroundColor = `rgba(73, 99, 239, ${1 - ((props.index + 1) * 0.1)})`;

  return (
    <div className="item__container" style={{ backgroundColor: adjustedBackgroundColor }}>
      <div className="item__value">
        {props.value}
      </div>
    </div>
  );
}

export default Item;