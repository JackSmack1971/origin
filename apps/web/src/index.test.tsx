import React from 'react';
/**
 * @jest-environment jsdom
 */
import '@testing-library/jest-dom';
import '@testing-library/jest-dom';
import ReactDOM from 'react-dom/client';
import { render, screen } from '@testing-library/react';

// this is just a little hack to silence a warning that we'll get until we
// upgrade to 16.9. See also: https://github.com/facebook/react/pull/14853
const originalError = console.error
beforeAll(() => {
  console.error = (...args) => {
    if (/Warning.*not wrapped in act/.test(args[0])) {
      return
    }
    originalError.call(console, ...args)
  }
})

afterAll(() => {
  console.error = originalError
})
import App from './App';

describe('Index Component', () => {
  it('renders without crashing', () => {
    render(<App />);
    const headingElement = screen.getByText(/Welcome to Creative Foundry!/i);
    expect(headingElement).toBeInTheDocument();
  });
});