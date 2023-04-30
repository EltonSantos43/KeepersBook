from django.test import TestCase, Client
from django.urls import reverse
from app.forms import SignupForm

class TestForms(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_signup_form_valid(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = SignupForm(data=data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        data = {
            'username': 'testuser',
            'email': 'invalidemail',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertIsInstance(response.context['form'], SignupForm)

    def test_signup_view_post(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

        response = self.client.post(self.signup_url, data=data)
        self.assertEqual(response.status_code, 302) # redireciona para a página de login após o cadastro
        self.assertRedirects(response, reverse('login'), status_code=302)
