import json

from ads.models import Advertisement, Review
from tests.base_test_case import BaseTestCase


class TestAdvertisement(BaseTestCase):
    """Тестирование модели объявлений."""

    def setUp(self):
        super().setUp()
        self.advertisement = self.create_advertisement(title="Товар")

    def test_str_advertisement(self):
        """Проверка метода __str__ модели Advertisement."""
        expected_str = f"{self.advertisement.title}"
        assert str(self.advertisement) == expected_str

    def test_create_advertisement(self):
        """Проверка создания объявления."""
        data = self.create_advertisement_data()
        response = self.client.post("/ads/", data=data)
        new_ads = Advertisement.objects.order_by("-id").first()
        assert response.status_code == 201
        assert new_ads.title == "Товар"
        assert new_ads.description == "Лучшее описание"
        assert Advertisement.objects.count() == 3

    def test_advertisement_list(self):
        """Проверка получения списка объявлений."""
        response = self.client.get("/ads/")
        content = response.content.decode("utf-8")
        data = json.loads(content)
        assert response.status_code == 200
        assert isinstance(data, dict)
        assert "results" in data
        assert isinstance(data["results"], list)

    def test_put_advertisement(self):
        """Проверка полного изменения объявления."""
        data = {
            "title": "Изменённое название",
            "price": 25,
            "description": "Изменённое описание",
        }
        ads_put = Advertisement.objects.order_by("-id").first()
        ads_id = ads_put.id
        response = self.client.put(f"/ads/{ads_id}/", data)
        ads_put.refresh_from_db()
        assert response.status_code == 200
        assert ads_put.title == "Изменённое название"
        assert ads_put.price == 25
        assert ads_put.description == "Изменённое описание"

    def test_patch_advertisement(self):
        """Проверка частичного изменения объявления."""
        data = {"title": "Другое название"}
        ads_path = Advertisement.objects.order_by("-id").first()
        ads_id = ads_path.id
        response = self.client.patch(f"/ads/{ads_id}/", data)
        ads_path.refresh_from_db()
        assert response.status_code == 200
        assert ads_path.title == "Другое название"

    def test_delete_advertisement(self):
        """Проверка удаления объявления."""
        ads_del = Advertisement.objects.order_by("-id").first()
        ads_id = ads_del.id
        response = self.client.delete(f"/ads/{ads_id}/")
        assert response.status_code == 204
        assert Advertisement.objects.count() == 1


class TestReview(BaseTestCase):
    """Тестирование модели отзывов на объявление."""

    def setUp(self):
        super().setUp()
        self.advertisement = self.create_advertisement(title="Товар")

    def test_create_review(self):
        """Проверка создания отзыва."""
        data = self.create_review_data()
        ads_review = Advertisement.objects.order_by("-id").first()
        ads_id = ads_review.id
        response = self.client.post(f"/ads/{ads_id}/reviews/", data)
        review = Review.objects.order_by("-id").first()
        assert response.status_code == 201
        assert review.text == "Тестовый отзыв"

    def test_path_review(self):
        """Проверка изменения отзыва."""
        data = self.create_review_data()
        data_path = {"text": "Изменённый отзыв"}
        ads_review = Advertisement.objects.order_by("-id").first()
        ads_id = ads_review.id
        response_post = self.client.post(f"/ads/{ads_id}/reviews/", data)
        review = Review.objects.order_by("-id").first()
        response_patch = self.client.patch(
            f"/ads/{ads_id}/reviews/{review.id}/", data_path
        )
        review.refresh_from_db()
        assert response_patch.status_code == 200
        assert review.text == "Изменённый отзыв"

    def test_del_review(self):
        """Проверка удаления отзыва."""
        data = self.create_review_data()
        ads_review = Advertisement.objects.order_by("-id").first()
        ads_id = ads_review.id
        response = self.client.post(f"/ads/{ads_id}/reviews/", data)
        review = Review.objects.order_by("-id").first()
        response_del = self.client.delete(
            f"/ads/{ads_id}/reviews/{review.id}/"
        )
        assert response_del.status_code == 204
