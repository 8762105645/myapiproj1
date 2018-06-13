from rest_framework import serializers
from . models import Users

class Usersserializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields=('firstname','lastname')
