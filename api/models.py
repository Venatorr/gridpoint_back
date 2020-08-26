from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class File(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Название файла')
    add_date = models.DateTimeField('added date', auto_now_add=True)

    class Meta:
        ordering = ['-add_date', ]
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name


class DataFile(models.Model):
    file_name = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='datafile')
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    i = models.IntegerField()

    class Meta:
        ordering = ['-id', ]
