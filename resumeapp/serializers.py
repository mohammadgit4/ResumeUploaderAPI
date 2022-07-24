from rest_framework import serializers
from .models import Profile

class ProfileSLR(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate(self, attrs):
        if Profile.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('Email is already Exists!')
        return attrs