from django.urls import path
from .views import (
    EventListCreateView,
    EventDetailView,
    RegistrationListCreateView,
    RegistrationDetailView,
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', RegistrationDetailView.as_view(), name='registration-detail'),
]