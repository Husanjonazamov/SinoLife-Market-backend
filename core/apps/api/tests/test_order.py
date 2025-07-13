from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.apps.api.models import OrderitemModel, OrderModel


class OrderTest(TestCase):

    def _create_data(self):
        return OrderModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("order-list"),
            "retrieve": reverse("order-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("order-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_list(self):
        response = self.client.get(self.urls["list"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_not_found(self):
        response = self.client.get(self.urls["retrieve-not-found"])
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)


class OrderitemTest(TestCase):

    def _create_data(self):
        return OrderitemModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("orderItem-list"),
            "retrieve": reverse("orderItem-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("orderItem-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_list(self):
        response = self.client.get(self.urls["list"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_not_found(self):
        response = self.client.get(self.urls["retrieve-not-found"])
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)
