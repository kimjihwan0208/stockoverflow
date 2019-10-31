import React from 'react';
import './List.css';
import Item from './Item/Item';

const numListItems = 7;

function List(props) {
  console.log("received list of terms from props", props.terms);

  return (
    <div className="list__container">
      <div className="row justify-content-center">
        {props.terms && props.terms.slice(0, numListItems).map(({ term, score }, index) => {
          return (
            <div className="col-10">
              <Item value={term} index={index} score={score} />
            </div>
          )
        })}
      </div>
    </div>
  );
}

export default List;