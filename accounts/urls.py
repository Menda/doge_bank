from django.urls import path
from .views import (ContactListView, ContactAddView, ContactUpdateView,
                    ContactDeleteView)

urlpatterns = [
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
    path('contact/add/', ContactAddView.as_view(), name='contact-add'),
    path('contact/<int:pk>/', ContactUpdateView.as_view(),
         name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(),
         name='contact-delete'),
]
