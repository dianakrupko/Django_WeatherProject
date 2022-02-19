from django.db import models


class Lviv(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Employee(models.Model):
    login = models.CharField('Логін', max_length=40)
    password = models.CharField('Пароль', max_length=40)

    def __str__(self):
        return self.login


class Kyiv(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Ivano_Frankivsk(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Dnipropetrovsk(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Donetsk(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Krivoy_rog(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Luhansk(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Odessa(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Kharkiv(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time


class Simferopol(models.Model):
    date_time = models.DateTimeField('Дата і час')
    T = models.IntegerField('Температура')
    dd = models.CharField('Напрям вітру', max_length=25)
    FF = models.IntegerField('Швидкість вітру')

    def __str__(self):
        return self.date_time