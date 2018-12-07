from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include(('accounts.urls', 'accounts'),
                              namespace='accounts')),
    path('admin/', admin.site.urls),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social/', include('social_django.urls', namespace='social')),
]
