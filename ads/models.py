from django.db import models


class Advertisement(models.Model):
    """Описывает объявление."""

    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    description = models.TextField(verbose_name="Описание товара")
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="advertisements",
        verbose_name="Автор объявления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания объявления"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Review(models.Model):
    """Описывает отзывы на объявления."""

    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор отзыва",
    )
    ad = models.ForeignKey(
        "Advertisement",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Отзыв на объявление",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания отзыва"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Review by {self.author} for {self.ad}"
