from ast import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#User Profile Model
# class UserProfile(models.Model):
#     profile_pic = models.ImageField(upload_to='profile_image', blank=True, null=True)
#     favoriteSet = models.CharField(max_length=100)


#Lego Model
class LegoSet(models.Model):
    title = models.CharField(max_length=100)
    theme = models.CharField(max_length=100) 
    pieces = models.IntegerField(default=0)
    rebrick_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# #Comment Model
# class Comment(models.Model):
#     content = models.TextField
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, related_name='comments', 
#     on_delete=models.CASCADE)
#     lego_set = models.ForeignKey(LegoSet, related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return  f"User: {self.author.username} commmented on Set: {self.lego_set.title}"

# #Collection Model
# class Collection(models.Model):
#     user = models.ForeignKey(User, related_name='collections', on_delete=models.CASCADE)
#     lego_set = models.ForeignKey(LegoSet, related_name='collections', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.user.username} owns Set: {self.lego_set.title}"

# #Likes Model
# class Likes(models.Model):
#     user = models.ForeignKey(User, related_name='saved', on_delete=models.CASCADE)
#     lego_set = models.ForeignKey(LegoSet, related_name='saved', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username} likes {self.lego_set.title}"