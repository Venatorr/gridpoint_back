from .models import File, DataFile, User
from .serializers import FileSerializer, DataFileSerializer, UserSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password

EMPTY_FILE_ID = -1


class FilesViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DataFileViewSet(viewsets.ModelViewSet):
    queryset = DataFile.objects.all()
    serializer_class = DataFileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        file_id = self.request.query_params.get('file-id', EMPTY_FILE_ID)
        return DataFile.objects.filter(file_name_id=file_id)


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def get_token(self, data):
        user = User.objects.get(username=data['username'])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        data['token'] = token
        return data

    def post(self, request):
        user = request.data
        user['password'] = make_password(user['password'])
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = self.get_token(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED)
