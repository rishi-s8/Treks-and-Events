from django.db import models
import datetime

class Trek(models.Model):
    place = models.CharField(max_length=200)
    duration = models.DurationField()
    card_pic = models.CharField(max_length=1500, default = '')

    def __str__(self):
        return self.place


class Pictures(models.Model):
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, default = 'jpg')
    credits = models.CharField(max_length=200, default = 'IDK')
    file_link = models.CharField(max_length=1500, default = '')

    def __str__(self):
        return self.file_type + '-' + self.credits


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    logo_link = models.CharField(max_length=1500, default = '')

    def __str__(self):
        return self.name + '-' + str(self.date)


class Pics(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, default = 'jpg')
    credits = models.CharField(max_length=200, default = 'IDK')
    file_link = models.CharField(max_length=1500, default = '')

    def __str__(self):
        return self.file_type + '-' + self.credits
