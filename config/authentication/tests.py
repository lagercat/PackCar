from django.test import TestCase
from django.contrib.auth.models import User

from .forms import LoginForm


class AuthFormsTestCase(TestCase):

    def setup(self):
        self.user = User.objects.create_user(username="tester",
                                             password="top_secret")

    def test_valid_login_form(self):
        form_data = {'username': 'tester', 'password': 'top_seret'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())