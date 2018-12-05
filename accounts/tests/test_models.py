from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import Contact


class ContactTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create(username="Rafito")

    def test_save_contact(self):
        data = {
            'first_name': 'Rafitö',
            'last_name': 'Muñoz',
            'iban': 'DE89 3704 0044 0532 0130 00',
            'created_by': self.user,
        }
        Contact.objects.create(**data)
        self.assertTrue(Contact.objects.filter(**data).exists())

    def test_save_contact_empty_first_name(self):
        self.assertRaises(
            IntegrityError,
            Contact.objects.create,
            first_name=None,
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user,
        )

    def test_save_contact_empty_last_name(self):
        self.assertRaises(
            IntegrityError,
            Contact.objects.create,
            first_name='Rafitö',
            last_name=None,
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user,
        )

    def test_save_contact_empty_iban(self):
        self.assertRaises(
            IntegrityError,
            Contact.objects.create,
            first_name='Rafitö',
            last_name='Muñoz',
            iban=None,
            created_by=self.user,
        )

    def test_save_contact_empty_created_by(self):
        self.assertRaises(
            IntegrityError,
            Contact.objects.create,
            first_name='Rafitö',
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
        )

    def test_contact_string_representation(self):
        contact = Contact(
            first_name='Rafitö',
            last_name='Muñoz',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=self.user,
        )
        contact.save()
        self.assertEqual(
            repr(contact), '<Contact: Rafitö Muñoz>')
