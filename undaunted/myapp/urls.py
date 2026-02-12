from django.urls import path
from .views import LandingView, DashboardView, ai_view, smart_notes_view

app_name = 'myapp'

urlpatterns = [
    path('', LandingView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('test/', ai_view, name='ai'),
    path('notes/',smart_notes_view, name='smart_notes'),
]