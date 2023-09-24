from rest_framework import serializers
from .models import User_app


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app
        fields = ['name', 'filing_status', 'estimated_year_income']
