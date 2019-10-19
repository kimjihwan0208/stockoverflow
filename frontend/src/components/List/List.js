import React from 'react';
import './List.css';
import Item from './Item/Item';
import { impactfulTerms } from '../../mocks/impactfulTerms';

function List() {
  return (
    <div className="list__container">
      <div className="row justify-content-center">
        {impactfulTerms && impactfulTerms.map((impactfulTerm, index) => {
          console.log(index)
          return (
            <div className="col-10">
              <Item value={impactfulTerm} index={index} />
            </div>
          )
        })}
      </div>
    </div>
  );
}

export default List;