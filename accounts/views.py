from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
