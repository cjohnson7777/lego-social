from django.db import models

# Create your models here.

#User Model


#Lego Model
class LegoSet(models.Model):
    title = models.CharField(max_length=100)
    collection = models.CharField(max_length=100) 
    pieces = models.IntegerField


#Comment Model
class Comment(models.Model):
    content = models.TextField
    #user - legoSet relationship

#Collection Model
class Collection(models.Model):
    #user - legoSet relationship
    pass

#Likes Model
class Likes(models.Model):
    #user - legoSet relationship
    pass