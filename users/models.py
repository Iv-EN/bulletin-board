from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class User(AbstractUser, PermissionsMixin):
    """Модель пользователя."""

    ROLE_CHOICES = (
        ("user", "User"),
        ("admin", "Admin"),
    )

    phone = models.CharField(max_length=20, verbose_name="Телефон для связи")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    role = models.CharField(
        max_length=5,
        choices=ROLE_CHOICES,
        default="user",
        verbose_name="Роль пользователя",
    )
    image = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Фото"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
