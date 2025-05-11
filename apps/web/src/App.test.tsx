/**
 * @jest-environment jsdom
 */
import '@testing-library/jest-dom';
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';
import { Button } from '@creativefoundry/ui';

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

describe('App Component', () => {
  it('renders welcome message', () => {
    render(
      <div>
        <App />
        <Button>Test Button</Button>
      </div>
    );
    const headingElement = screen.getByText(/Welcome to Creative Foundry!/i);
    expect(headingElement).toBeInTheDocument();
  });

  it('should allow a user to enroll in MFA', () => {
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const promptSpy = jest.spyOn(window, 'prompt').mockReturnValue('email');
    render(<App />);
    const enrollButton = screen.getByText(/Enroll in MFA/i);
    enrollButton.click();
    promptSpy.mockRestore();
    alertSpy.mockRestore();
  });

  it('should allow a user to select their preferred MFA method', () => {
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const promptSpy = jest.spyOn(window, 'prompt').mockReturnValue('email');
    render(<App />);
    const enrollButton = screen.getByText(/Enroll in MFA/i);
    enrollButton.click();
    expect(promptSpy).toHaveBeenCalled();
    promptSpy.mockRestore();
    alertSpy.mockRestore();
  });

  it('should display an error message if the user provides invalid information during enrollment', () => {
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const promptSpy = jest.spyOn(window, 'prompt').mockReturnValue('invalid');
    render(<App />);
    const enrollButton = screen.getByText(/Enroll in MFA/i);
    enrollButton.click();
    expect(alertSpy).toHaveBeenCalledWith('Invalid MFA method selected!');
    promptSpy.mockRestore();
    alertSpy.mockRestore();
  });

  it('should validate the hardcoded verification code', () => {
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const promptSpy = jest.spyOn(window, 'prompt').mockReturnValueOnce('email').mockReturnValueOnce('123456'); // Hardcoded verification code
    render(<App />);
    const enrollButton = screen.getByText(/Enroll in MFA/i);
    enrollButton.click();
    expect(alertSpy).toHaveBeenCalledWith('Verification code validated!'); // Expect success
    promptSpy.mockRestore();
    alertSpy.mockRestore();
  });

  it('should display an error message if the user enters an invalid verification code', () => {
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const promptSpy = jest.spyOn(window, 'prompt').mockReturnValueOnce('email').mockReturnValueOnce('invalid');
    render(<App />);
    const enrollButton = screen.getByText(/Enroll in MFA/i);
    enrollButton.click();
    expect(alertSpy).toHaveBeenCalledWith('Invalid verification code!');
    promptSpy.mockRestore();
    alertSpy.mockRestore();
  });
});