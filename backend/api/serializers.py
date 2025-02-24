from dataclasses import fields
from pyclbr import Class
from pyexpat import model
from urllib import response
from rest_framework import serializers
from .models import LegoSet #, Likes, Collection, Comment
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]
#         extra_kwargs = {"password": {"write_only": True}}

class LegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoSet
        fields = ['rebrick_id', 'title', 'theme', 'pieces']
    
# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     lego_set = LegoSerializer()

#     class Meta:
#         model = Comment
#         fields = ['content', 'created_at', 'user', 'lego_set'] 

# class CollectionSerializer(serializers.ModelSerializer):
#     lego_set = LegoSerializer()

#     class Meta:
#         model = Collection
#         fields = ['user', 'lego_set']

# class LikesSerializer(serializers.ModelSerializer):
#     lego_set = LegoSerializer()

#     class Meta:
#         model = Likes
#         fields = ['user', 'lego_set']
