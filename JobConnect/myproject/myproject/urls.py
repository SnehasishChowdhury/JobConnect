from accounts.views import register_view
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView  # Import the LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),  # Use LoginView for root URL
    path('register/', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
