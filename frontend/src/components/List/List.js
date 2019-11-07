import React from 'react';
import './List.css';
import Item from './Item/Item';
import { impactfulTerms } from '../../mocks/impactfulTerms';

const numListItems = 7;

function List(props) {
  const { terms } = props;

  const impactfulTerms = terms.map(item => Object.entries(item)).slice(0, numListItems);

  return (
    <div className="list__container">
      <div className="row justify-content-center">
        {impactfulTerms.length > 0 && impactfulTerms.map((item, index) => {
          return (
            <div className="col-10">
              <Item value={item[0][0]} index={index} score={item[0][1]} />
            </div>
          )
        })}
      </div>
    </div>
  );
}

export default List;