from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Kino
from . serializers import KinoSerializer


# Create your views here.
    
def home_view(request):
    return render(request, 'kinoCRUD/post_list.html', {})     #String html

class KinoList(APIView):
    
    def get(self, request):
        Kino1 = Kino.objects.all()
        serializer=KinoSerializer(Kino1, many= True)
        return Response(serializer.data)
    
    
    def post(self):
        pass