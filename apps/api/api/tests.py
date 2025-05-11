from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        path = reverse('hero-list')
        # self.assertEqual(resolve(path).func, list)

    def test_detail(self):
        path = reverse('hero-detail', kwargs={'pk': 1})
        # self.assertEqual(resolve(path).func, detail)

    def test_generate_mfa_code(self):
        url = reverse('generate_mfa_code')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'MFA code generated successfully.')

    def test_validate_mfa_code_invalid(self):
        # Generate MFA code
        url_generate = reverse('generate_mfa_code')
        self.client.post(url_generate, format='json')

        # Attempt to validate with an invalid MFA code
        url = reverse('validate_mfa_code')
        data = {'mfa_code': 'invalid', 'user_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_validate_mfa_code_valid(self):
        # Generate MFA code
        url_generate = reverse('generate_mfa_code')
        response_generate = self.client.post(url_generate, format='json')
        self.assertEqual(response_generate.status_code, 200)

        # Get the generated MFA code from the session (not ideal for testing, but works for now)
        session = self.client.session
        mfa_code = session.get('mfa_code')
        self.assertIsNotNone(mfa_code)

        # Attempt to validate with the correct MFA code
        url = reverse('validate_mfa_code')
        data = {'mfa_code': mfa_code, 'user_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)  # Expect success
        self.assertEqual(response.data['message'], 'MFA code validated successfully.')

    def test_validate_mfa_code_bypass(self):
        # Generate MFA code
        url_generate = reverse('generate_mfa_code')
        response_generate = self.client.post(url_generate, format='json')
        self.assertEqual(response_generate.status_code, 200)

        # Attempt to bypass MFA with the hardcoded code
        url = reverse('validate_mfa_code')
        data = {'mfa_code': '123456', 'user_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)  # Expect failure

    def test_validate_mfa_code_invalid(self):
        # Generate MFA code
        url_generate = reverse('generate_mfa_code')
        response_generate = self.client.post(url_generate, format='json')
        self.assertEqual(response_generate.status_code, 200)

        # Attempt to validate with an invalid MFA code
        url = reverse('validate_mfa_code')
        data = {'mfa_code': 'invalid', 'user_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)