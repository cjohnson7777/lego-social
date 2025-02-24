from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import LegoSet
from .utils import get_data_from_rebrick
from .serializers import LegoSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def get_nothing(request):
    return Response(request.data)

@api_view(['GET'])
def get_sets(request):
     sets = LegoSet.objects.all()
     serializer = LegoSerializer(sets, many=True)
     return Response(serializer.data)

@api_view(['GET'])
def get_set(request, rid):
        try:
             lego_set = LegoSet.objects.get(rebrick_id=rid)
             serializer = LegoSerializer(lego_set)
             return Response(serializer.data)
        except LegoSet.DoesNotExist:
            data = get_data_from_rebrick(rid)

            if data:
                data = LegoSet.objects.create(
                    title = data.get('name', ''),
                    theme = data.get('theme_id', ''),
                    pieces = data.get('num_parts', 0),
                    rebrick_id = rid
                ) 

                serializer = LegoSerializer(data)
                return Response(serializer.data)
            return Response({"error": "Lego set not found"}, status=404)
