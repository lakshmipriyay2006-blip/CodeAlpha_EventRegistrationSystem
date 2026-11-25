from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        queryset = Registration.objects.all().order_by('-registered_at')
        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(email=email)
        return queryset


class RegistrationDetailView(generics.RetrieveDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Registration cancelled successfully."}, status=status.HTTP_200_OK)