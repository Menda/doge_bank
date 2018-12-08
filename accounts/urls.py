from django.urls import path
from .views import ContactListView

urlpatterns = [
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
]
