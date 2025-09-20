from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('user-list')
    payload = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    resp = api_client.post(url, payload, format='json')
    assert resp.status_code == status.HTTP_201_CREATED

    User = get_user_model()
    user = User.objects.get(username='testuser')
    assert user.email == payload['email']
    assert user.check_password(payload['password'])  