from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from arbitrage import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view redirects to the dashboard
    path('admin/', admin.site.urls),
    path('arbitrage/', include('arbitrage.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
