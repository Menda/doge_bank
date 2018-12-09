from django.urls import path
from .views import ContactListView, ContactAddView, ContactUpdateView

urlpatterns = [
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
    path('contact/add/', ContactAddView.as_view(), name='contact-add'),
    path('contact/<int:pk>/', ContactUpdateView.as_view(),
         name='contact-update'),
]
