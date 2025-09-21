from rest_framework.test import APITestCase

from users.models import User
from ads.models import Advertisement


class BaseTestCase(APITestCase):
    """Базовый тестовый класс."""

    def setUp(self):
        """Метод для инициализации тестов."""
        self.user = self.create_user()
        self.client.force_authenticate(user=self.user)
        self.advertisement = self.create_advertisement()

    def create_user(self, **kwargs):
        """Создание пользователя с заданными параметрами."""
        default_data = {
            "username": "test_user",
            "email": "test_email",
            "password": "test",
            "phone": "123456789"
        }
        default_data.update(kwargs)
        return User.objects.create(**default_data)

    def create_advertisement(self, **kwargs):
        """Создание объявления с заданными параметрами."""
        default_data = {
            "author": self.user,
            "title": "Тестовое название",
            "price": 10,
            "description": "Тестовое описание",
        }
        default_data.update(kwargs)
        return Advertisement.objects.create(**default_data)

    def create_advertisement_data(self, **kwargs):
        """
        Метод для создания данных объявления с учетом переданных параметров.
        """
        default_data = {
            "author": self.user,
            "title": "Товар",
            "price": 100,
            "description": "Лучшее описание",
        }
        default_data.update(kwargs)
        return default_data

    def create_review_data(self, **kwargs):
        """
        Метод для создания данных отзыва с учетом переданных параметров.
        """
        default_data = {
            "author": self.user,
            "text": "Тестовый отзыв",
        }
        default_data.update(kwargs)
        return default_data

