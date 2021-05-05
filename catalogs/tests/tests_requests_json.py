from django.urls import reverse
from catalogs.models import Course, Catalog
from rest_framework import status
from rest_framework.test import APITestCase
from catalogs.api import urls


def test_update_data_to_course(client):
    url = reverse("catalogs-api:course-list")
    payload = {'title_course': 'Title Course 4',
               'date_start': '2021-06-01',
               'date_end': '2021-06-08',
               'quantity': 5}

    response = client.post(url, payload, format="json")

    assert response.status_code == 201

def test_list_course(client):
    url = reverse("catalogs-api:course-list")

    response = client.get(url, format="json")

    assert response.status_code == 200
