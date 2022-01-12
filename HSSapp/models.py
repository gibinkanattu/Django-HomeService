from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class State(models.Model):
    """To display the default states"""
    statename = models.CharField(max_length=20)

    def __str__(self):
        return self.statename


class District(models.Model):
    """To display the districts corresponding to the state"""
    statename = models.ForeignKey(State, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=20)

    def __str__(self):
        return self.districtname


class Area(models.Model):
    """To display the area to that of state and district"""
    statename = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    areaname = models.CharField(max_length=20)

    def __str__(self):
        return self.areaname


class JobCategory(models.Model):
    """Gives various job categories or service categories available"""
    job = models.CharField(max_length=50)

    def __str__(self):
        return self.job


class Profile(models.Model):
    """Created to store the location and job of the user"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    job = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.name} {0.phone} {0.job} '
        return template.format(self)


class Location(models.Model):
    """Store the location of user"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    place = models.CharField(max_length=50)

    def __str__(self):
        template = '{0.name} {0.state} {0.district} {0.area} {0.place}'
        return template.format(self)


class Feedback(models.Model):
    """To store the feedback of the user from other customers"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    customername = models.CharField(max_length=20)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.comment, self.rating


class Notification(models.Model):
    """To store the customers demand such as push notifications"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    customername = models.CharField(max_length=20)
    notice = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.notice


class Chat(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    customername = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.message


class Order(models.Model):
    """Store the details of the service providers booked or consulted"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    workername = models.ForeignKey(Profile, on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True)
    date = models.DateField(default=datetime.now())
    wage = models.IntegerField()

    def __str__(self):
        return self.name, self.workername, self.date


class RequestWork(models.Model):
    """ Store the request of the user that is to be sent as notification"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.notice
