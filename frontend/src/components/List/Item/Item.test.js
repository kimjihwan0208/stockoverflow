import React from 'react';
import { render } from '@testing-library/react';
import Item from './Item';
import { mockItemProps } from '../../../mocks/mockItem';

describe("Item", () => {
  it("renders", () => {
    const { baseElement } = render(<Item { ...mockItemProps }/>);
    expect(baseElement).toMatchSnapshot();
  })
});