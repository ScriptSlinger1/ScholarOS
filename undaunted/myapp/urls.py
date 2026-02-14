from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (LandingView,
                    DashboardView,
                    ai_view,
                    about,
                    contact,
                    demo,
                    profile_view,
                    smart_notes_view,
                    RegistrationView)

app_name = 'myapp'

urlpatterns = [
    path('', LandingView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('app_eval/', ai_view, name='ai'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('demo/', demo, name='demo'),
    path('profile/', profile_view, name='profile'),
    path('notes/',smart_notes_view, name='smart_notes'),
    path('reg/', RegistrationView.as_view(), name='reg'),
    path('login/', LoginView.as_view(template_name='myapp/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]