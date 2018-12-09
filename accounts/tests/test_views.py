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


class ContactAddViewTest(TestCase):
    def setUp(self):
        self.url = reverse('accounts:contact-add')
        user_model = get_user_model()
        self.user = user_model.objects.create(username='Rafito')

    def test_add_contact(self):
        self.client.force_login(self.user)
        data = {
            'first_name': 'Rafitö',
            'last_name': 'Muñoz',
            'iban': 'DE89 3704 0044 0532 0130 00',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         reverse('accounts:contact-list'))

        self.assertTrue(Contact.objects.filter(**data).exists())

    def test_add_contact_missing_fields(self):
        self.client.force_login(self.user)
        data = {
            'first_name': 'Rafitö',
            'last_name': 'Muñoz',
            'iban': 'DE89 3704 0044 0532 0130 00',
        }

        for key in data.keys():
            data_modified = data.copy()
            data_modified[key] = ''
            response = self.client.post(self.url, data_modified)
            self.assertEqual(response.status_code, 200)
            self.assertFalse(response.context_data['form'].is_valid())

        self.assertFalse(Contact.objects.filter(**data).exists())

    def test_not_authorised(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         f"{settings.LOGIN_URL}?next={self.url}")


class ContactUpdateViewTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create(username='Rafito')

        self.contact = Contact.objects.create(
            first_name='Rafitö',
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user)
        self.url = reverse('accounts:contact-update', args=[self.contact.pk])

    def test_update(self):
        self.client.force_login(self.user)
        data = {
            'first_name': 'Jamés',
            'last_name': 'Brówñ',
            'iban': 'ES91 2100 0418 4502 0005 1332',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         reverse('accounts:contact-list'))

        contact = Contact.objects.get(pk=self.contact.pk)
        self.assertEqual(contact.first_name, data['first_name'])
        self.assertEqual(contact.last_name, data['last_name'])
        self.assertEqual(contact.iban, data['iban'].replace(' ', ''))

    def test_update_missing_fields(self):
        self.client.force_login(self.user)
        data = {
            'first_name': 'Jamés',
            'last_name': 'Brówñ',
            'iban': 'ES91 2100 0418 4502 0005 1332',
        }

        for key in data.keys():
            data_modified = data.copy()
            data_modified[key] = ''
            response = self.client.post(self.url, data_modified)
            self.assertEqual(response.status_code, 200)
            self.assertFalse(response.context_data['form'].is_valid())

        contact = Contact.objects.get(pk=self.contact.pk)
        self.assertEqual(contact.first_name, self.contact.first_name)
        self.assertEqual(contact.last_name, self.contact.last_name)
        self.assertEqual(contact.iban, self.contact.iban.replace(' ', ''))

    def test_not_same_user_as_created_by(self):
        user_model = get_user_model()
        user_other = user_model.objects.create(username='Bowie')
        self.contact.created_by = user_other
        self.contact.save()

        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_not_found(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('accounts:contact-update', args=[123456]))
        self.assertEqual(response.status_code, 404)

    def test_not_authorised(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         f"{settings.LOGIN_URL}?next={self.url}")


class ContactDeleteViewTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create(username='Rafito')

        self.contact = Contact.objects.create(
            first_name='Rafitö',
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user)
        self.url = reverse('accounts:contact-delete', args=[self.contact.pk])

    def test_delete_confirmation_page_shows_up(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         reverse('accounts:contact-list'))
        self.assertRaises(
            Contact.DoesNotExist,
            Contact.objects.get,
            pk=self.contact.pk)

    def test_not_found(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('accounts:contact-delete', args=[123456]))
        self.assertEqual(response.status_code, 404)

    def test_not_authorised(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         f"{settings.LOGIN_URL}?next={self.url}")
