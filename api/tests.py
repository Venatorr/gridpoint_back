from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from api.models import User, File, DataFile


class TestApi(APITestCase):
    def setUp(self):
        self.auth_client = APIClient()
        test_user = {'username': 'test_user', 'password': '12345'}
        self.user = User.objects.create_user(
            username=test_user['username'],
            password=test_user['password'])
        self.file = File.objects.create(name='test_file.test')
        self.datafile = DataFile.objects.create(
            file_name=self.file, x=0, y=0, z=0, i=0)
        self.auth_client.force_authenticate(user=self.user)
        self.unauth_client = APIClient()


    def test_signup(self):
        data = {'username': 'new_test_user', 'password': '12345'}
        self.response = self.unauth_client.post(
            reverse('signup'),
            format='json',
            data=data,
            follow=True)
        message = 'Cannot signup user'
        self.assertEqual(self.response.status_code, 201, msg=message)
        is_exist = User.objects.filter(username=data['username']).exists()
        self.assertTrue(is_exist, msg=message)

    def test_auth_access(self):
        self.response = self.auth_client.get(
            reverse('file-list'), params={'page': 1})
        message = 'Authorize client does not see files'
        self.assertEqual(
            self.response.data['count'], 1, msg=message)

        self.response = self.auth_client.get(
            reverse('datafile-list') + f'?file-id={self.file.id}')
        message = 'Authorize client does not see datafile'
        self.assertEqual(
            self.response.data['count'], 1, msg=message)

    def test_unauth_access(self):
        self.response = self.unauth_client.get(
            reverse('file-list'), params={'page': 1})
        message = 'Unauthorize client should not see files'
        self.assertEqual(
            self.response.status_code, 401, msg=message)

        self.response = self.unauth_client.get(
            reverse('datafile-list') + f'?file-id={self.file.id}')
        message = 'Unauthorize client should not see data file'
        self.assertEqual(
            self.response.status_code, 401, msg=message)
