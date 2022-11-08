from rest_framework import serializers
from .models import DonorRegister, Donor

class DonorRegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DonorRegister
        fiels = {
            'full_name',
            'email',
            'password'
        }