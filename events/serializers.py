from rest_framework import serializers
from .models import Event, Registration


class EventSerializer(serializers.ModelSerializer):
    registered_count = serializers.IntegerField(source='registrations.count', read_only=True)
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'capacity',
            'registered_count',
            'available_seats',
        ]

    def get_available_seats(self, obj):
        return obj.capacity - obj.registrations.count()


class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'event', 'event_title', 'full_name', 'email', 'phone', 'registered_at']

    def validate(self, data):
        event = data['event']
        if event.registrations.count() >= event.capacity:
            raise serializers.ValidationError("This event has reached full capacity.")
        return data