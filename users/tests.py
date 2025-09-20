from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ads.models import Advertisement, Review
from .models import User


class BaseTestCase(APITestCase):
    """Базовый тестовый класс."""

    def setUp(self):
        """Метод для инициализации тестов."""

        self.user = User.objects.create(
            username="test_user", email="test@test.ru", password="test"
        )
        self.ad = Advertisement.objects.create(
            title="test_ad", description="test description", author=self.user,
            price=10
        )
        self.review = Review.objects.create(
            text="test_text"
        )
        self.client.force_authenticate(user=self.user)


class TestUser(BaseTestCase):
    """Тестирование модели курса."""

    def test_create_user(self):
        """Проверка создания нового пользователя."""

        data = {
            "username": "new_test_user",
            "email": "test@email.ru",
            "password": "test",
        }
        response = self.client.post("/users/user/", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.last().username, "new_test_user")
        self.assertEqual(User.objects.last().email, "test@email.ru")
        self.assertEqual(User.objects.count(), 2)