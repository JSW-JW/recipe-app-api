from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user within email is successful"""
        email = 'test@exam.com'
        password = 'tmd8246!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EXAM.cOm'
        user = get_user_model().objects.create_user(email, 'tmd8246!')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            # anything we do here should raise ValueError.
            get_user_model().objects.create_user(None, 'tmd8246!')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'vics8246@gmail.com',
            'tmd8246!'
        )

        self.assertTrue(user.is_superuser)
        # is_superuser is included by PermissionsMixin
        self.assertTrue(user.is_staff)
