from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Master(models.Model):
    RANK_CHOICES = (
        (0, 'Rank 1'),
        (1, 'Rank 2'),
    )
    name = models.CharField(max_length=100)
    rank = models.IntegerField(default=0, choices=RANK_CHOICES)
    phone = models.IntegerField()
    status = models.BooleanField(default=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Booking(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.master


class Calendar(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time_start = models.TimeField()
    time_end = models.TimeField()

