from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_jwt.views import (obtain_jwt_token,
    refresh_jwt_token, verify_jwt_token)
from django.conf.urls import url

router = DefaultRouter()
router.register(r'files', views.FilesViewSet, basename='file')
router.register(r'datafile', views.DataFileViewSet, basename='datafile')

urlpatterns = router.urls
urlpatterns = [
    path('signup/', views.CreateUserAPIView.as_view(), name='signup'),
    url(r'^obtain-jwt-token/', obtain_jwt_token, name='obtain-jwt-token'),
    url(r'^refresh-jwt-token/', refresh_jwt_token, name='refresh-jwt-token'),
    url(r'^verify-jwt-token/', verify_jwt_token, name='verify-jwt-token'),
              ] + urlpatterns
