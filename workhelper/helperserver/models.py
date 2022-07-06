from django.db import models
from django.conf import settings
from django.utils import timezone


class Order(models.Model):
    master_name = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Мастер', on_delete=models.PROTECT)
    client_name = models.CharField(verbose_name='Клиент', max_length=200)
    device_type = models.CharField(verbose_name='Тип устройства', max_length=200)
    date_start = models.DateField(verbose_name='Дата начала работ', blank=True, null=True)
    defect = models.TextField(verbose_name='Заявленная неисправность')
    completed_work_text = models.TextField(verbose_name='Проделанная работа')
    spare_parts_text = models.TextField(verbose_name='Закупленные запчасти')
    income = models.IntegerField(verbose_name='Приход')
    consumption = models.IntegerField(verbose_name='Расход')
    total = models.IntegerField(verbose_name='Итого')
    date_finish = models.DateField(verbose_name='Дата окончания работ', blank=True, null=True)
    def __str__(self):
        return self.device_type


class Complited_work(models.Model):
    order_name = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name='Название работы')
    price = models.IntegerField(verbose_name='Стоимость работы')


class Spare_parts(models.Model):
    part_name = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name='Наименование запчасти')
    price = models.IntegerField(verbose_name='Стоимость запчасти')
