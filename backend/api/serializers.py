from rest_framework import serializers
from models import LegoSet, Likes, Collection, Comment

def get_data_from_rebrick(id):
    pass
    #check if set id is in database, if yes return instance

    #call the api, save the data, return it

class LegoSerializer(serializers.ModelSerializer):
    model = LegoSet
    fields = []

    def to_representation(self, instance):
        rep = instance

        if not rep:
            data = get_data_from_rebrick()

        if data:
            pass
        
        return data
    
class CommentSerializer(serializers.ModelSerializer):
    pass

class CollectionSerializer(serializers.ModelSerializer):
    pass

class LikesSerializer(serializers.ModelSerializer):
    pass
