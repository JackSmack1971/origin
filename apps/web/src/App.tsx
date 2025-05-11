import React from 'react';
import Button from '@creativefoundry/ui/src/button';


function App(): React.ReactNode {
  return (
    <div>
      <h1>Welcome to Creative Foundry!</h1>
      <Button onClick={enrollMFA}>Enroll in MFA</Button>
    </div>
  );
}

// Add MFA enrollment logic here
/**
 * Handles the MFA enrollment process.
 */
function enrollMFA() {
  alert('Enrolling in MFA!');

  // Prompt the user to select an MFA method.
  const mfaMethod = prompt('Select MFA method: (email/sms)');

  // Validate the selected MFA method.
  if (mfaMethod !== 'email' && mfaMethod !== 'sms') {
    alert('Invalid MFA method selected!');
    return;
  }
  alert(`Selected MFA method: ${mfaMethod}`);

  // Prompt the user to enter a verification code.
  const verificationCode = prompt('Enter verification code:');

  // Validate the verification code on the server.
  fetch('/api/validate_mfa_code/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      mfa_code: verificationCode,
      user_id: 'testuser' // Replace with actual user ID
    })
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message);
  })
  .catch(error => {
    alert('Error validating MFA code: ' + error);
  });
}

export default App;