from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Specialist(models.Model):
    RANK_CHOICES = (
        (1, 'Rank 1'),
        (2, 'Rank 2'),
    )
    STATUS_CHOICES = (
        (1, 'Status 1'),
        (2, 'Status 2'),
        (3, 'Status 3'),
        (4, 'Status 4'),
    )
    name = models.CharField(max_length=100)
    rank = models.IntegerField(default=0, choices=RANK_CHOICES)
    phone = models.IntegerField()
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Booking(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.specialist.name


class WorkSchedule(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
