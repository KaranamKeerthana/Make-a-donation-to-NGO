from django.db import models

# Create your models here.
class NGO(models.Model):
    name=models.CharField(max_length=330)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    district=models.CharField(max_length=90)

    def __str__(self):
        return self.username

class Public(models.Model):
    name1=models.CharField(max_length=50)
    username1=models.CharField(max_length=50,unique=True)
    email1=models.EmailField(max_length=50)
    password1=models.CharField(max_length=30)
    district1=models.CharField(max_length=90)

    def __str__(self):
        return self.username1

class Volunteer(models.Model):
    name2=models.CharField(max_length=50)
    username2=models.CharField(max_length=50,unique=True)
    email2=models.EmailField(max_length=50)
    password2=models.CharField(max_length=30)
    district2=models.CharField(max_length=60)

    

    def __str__(self):
        return self.username2


class Event(models.Model):
    name4=models.CharField(max_length=50)
    mobile4=models.CharField(max_length=10)
    address4=models.CharField(max_length=420)
    date4=models.DateField(max_length=30)
    time4=models.TimeField(max_length=30)

    def get_values(self):
        
        return Event.objects.all().values()
    def get_length(self):
        return 4

    def __str__(self):
        return self.name4


class Gathering(models.Model):
    name5=models.CharField(max_length=330)
    place5=models.CharField(max_length=330)
    cause5=models.CharField(max_length=920)
    date5=models.DateField(max_length=30)
    time5=models.TimeField(max_length=30)
    def get_values1(self):
        
        return Gathering.objects.all().values()
    def get_length1(self):
        return 4

    def __str__(self):
        return self.name5