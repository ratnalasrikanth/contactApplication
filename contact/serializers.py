from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["country","phone_number","first_name","last_name","is_favourite","contact_picture"]