#Serializers are basically used to convert complex data to native Python datatypes 
# that can then be easily rendered into JSON(Which we are going to use in React i.e. 
# Client side). 

from rest_framework import serializers
from .models import url

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = url
        fields = '__all__'