from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@django.com', password='password'):
    """ Create a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with email is successfull """
        email = 'brett@test.com'
        password = 'Password1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'brett.minor@AMAZON.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='asfdbasefsdf'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "asdf")

    def test_create_new_superuser(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            'brett@test.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """" Test the ingredient string representation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """ Test the recipe string representation """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and Mushroom Sauce',
            time_minutes=5,
            price=12.99
        )

        self.assertEqual(str(recipe), recipe.title)
