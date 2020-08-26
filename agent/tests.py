import tempfile

from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import File, DataFile
from datetime import datetime
import random


class TestAgent(APITestCase):
    def test_adding_file(self):
        with tempfile.NamedTemporaryFile(delete=True) as tmp:
            tmp.write('1 2 3 4'.encode())
            tmp.seek(0)
            self.client.post(reverse('upload'), {'file': tmp})
            tmp.close()
            is_file_exist = File.objects.filter().exists()
            is_data_exist = DataFile.objects.filter().exists()
            message = 'Upload file is not working'
            self.assertTrue(is_file_exist, msg=message)
            self.assertTrue(is_data_exist, msg=message)

    def test_adding_wrong_file(self):
        '''
        Добавление файла с некорректной структурой
        '''
        with tempfile.NamedTemporaryFile(delete=True) as tmp:
            tmp.write('1 1'.encode())
            tmp.seek(0)
            self.client.post(reverse('upload'), {'file': tmp})
            tmp.close()
            is_file_exist = File.objects.filter().exists()
            is_data_exist = DataFile.objects.filter().exists()
            message = 'File with wrong structure should not be uploaded'
            self.assertFalse(is_file_exist, msg=message)
            self.assertFalse(is_data_exist, msg=message)

    def test_stress_volume(self):
        '''
        Нагрузочный тест. Проверяет, что при линейном росте кол-ва строк
        в файле, время его загрузки на сервер растет не более чем линейно
        '''
        count2time = {10000: 1,
                      100000: 10,
                      1000000: 100}
        message = 'Adding file is too long'
        for count, time in count2time.items():
            with tempfile.NamedTemporaryFile(delete=True) as tmp:
                for _ in range(count):
                    x = random.randint(0, 10000)
                    y = random.randint(0, 10000)
                    z = random.randint(0, 10000)
                    i = random.randint(1, 255)
                    tmp.write(f'{x} {y} {z} {i}\n'.encode())
                tmp.seek(0)
                start_time = datetime.now()
                self.client.post(reverse('upload'), {'file': tmp})
                result_time = (datetime.now() - start_time).total_seconds()
                tmp.close()
                self.assertLess(result_time, time, msg=message)
