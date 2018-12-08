from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Contact


class ContactListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('accounts:contact-list')
        user_model = get_user_model()
        self.user = user_model.objects.create(username='Rafito')

    def test_list_contacts_empty(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_list_contacts(self):
        contact = Contact.objects.create(
            first_name='Rafitö',
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user)

        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['object_list'],
            [repr(contact)])

    def test_not_authorised(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(response['location'],
                         f"{settings.LOGIN_URL}?next={self.url}")
