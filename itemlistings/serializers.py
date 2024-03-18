from rest_framework import serializers
from .models import main
class carribeanSerializer(serializers.ModelSerializer):
    class Meta:
        model=main
        fields = '__all__'#use(fieldname1,fieldname2...)for specific fields