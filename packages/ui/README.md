# Button Component

This component is a simple button that can be used in your React applications.

## Usage

```tsx
import Button from '@your-org/ui/button';

const MyComponent = () => {
  return (
    <Button onClick={() => alert('Clicked!')}>Click me</Button>
  );
};
```

## Props

| Name       | Type               | Description                               |
| ----------- | ------------------ | ----------------------------------------- |
| children   | React.ReactNode    | The content of the button.                |
| onClick    | () => void         | The function to call when the button is clicked. |
| disabled   | boolean            | Whether the button is disabled.           |

## Testing

This component uses Jest for testing. There was a configuration issue with Jest that caused the tests to fail. This issue has been resolved by adding the following comment to the top of the test file:

```tsx
/**
 * @jest-environment jsdom
 */
```

This tells Jest to use the jsdom environment for the tests, which is necessary for components that use the DOM.