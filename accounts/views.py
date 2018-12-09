from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

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


class ContactUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                        UpdateView):
    template_name_suffix = '_update'
    model = Contact
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('accounts:contact-list')

    def has_permission(self):
        try:
            contact = Contact.objects.get(pk=self.kwargs['pk'])
        except Contact.DoesNotExist:
            # 404 will be raised at other layer
            return True
        else:
            if contact.created_by == self.request.user:
                return True
            else:
                return False


class ContactDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                        DeleteView):
    model = Contact
    success_url = reverse_lazy('accounts:contact-list')

    def has_permission(self):
        try:
            contact = Contact.objects.get(pk=self.kwargs['pk'])
        except Contact.DoesNotExist:
            # 404 will be raised at other layer
            return True
        else:
            if contact.created_by == self.request.user:
                return True
            else:
                return False
