from django.urls import path
from .views import ContactListView, ContactAddView

urlpatterns = [
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
    path('contact/add/', ContactAddView.as_view(), name='contact-add'),
]
