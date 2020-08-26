from rest_framework import serializers
from .models import File, DataFile, User


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'add_date')
        read_only_fields = ('id',)


class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFile
        fields = ('id', 'x', 'y', 'z', 'i')
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}
