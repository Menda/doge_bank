from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact


class ContactAddView(LoginRequiredMixin, CreateView):
    template_name_suffix = '_add'
    model = Contact
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('accounts:contact-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
