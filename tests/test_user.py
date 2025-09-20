from users.models import User


def test_create_user(self):
    """Проверка создания нового пользователя."""
    data = {
        "username": "new_test_user",
        "email": "test@email.ru",
        "password": "test",
        "phone": "9999999999"
    }
    response = self.client.post("/users/register/", data=data)
    assert response.status_code == 201
    assert User.objects.last().username == "new_test_user"
    assert User.objects.count() == 1