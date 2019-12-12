from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *

# Create your views here.
    
def home_view(request):
    return render(request, 'kinoCRUD/post_list.html', {})     #String html
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class KinoList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        Kino1 = Kino.objects.all()
        serializer=KinoSerializer(Kino1, many= True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer= KinoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinoDetail(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Kino.objects.get(pk=pk)
        except Kino.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Kino = self.get_object(pk)
        serializer = KinoSerializer(Kino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Kino = self.get_object(pk)
        Kino.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeansList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        seans = Seans.objects.all()
        serializer=SeansPostSerializer(seans, many= True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer= SeansPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SeansDetail(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Seans.objects.get(pk=pk)
        except Seans.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Seans = self.get_object(pk)
        serializer = SeansPostSerializer(Seans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Seans = self.get_object(pk)
        Seans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilmList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        film1 = Film.objects.all()
        serializer=FilmPostSerializer(film1, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= FilmPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmDetail(APIView):

    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Film = self.get_object(pk)
        serializer = FilmPostSerializer(Film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Film = self.get_object(pk)
        Film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiejsceList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        miejsce = Miejsce.objects.all()
        serializer=MiejscePostSerializer(miejsce, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= MiejscePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MiejsceDetail(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Miejsce.objects.get(pk=pk)
        except Miejsce.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Miejsce = self.get_object(pk)
        serializer = MiejscePostSerializer(Miejsce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Miejsce = self.get_object(pk)
        Miejsce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SalaList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        sala = Sala.objects.all()
        serializer=SalaPostSerializer(sala, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= SalaPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaDetail(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Sala.objects.get(pk=pk)
        except Sala.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Sala = self.get_object(pk)
        serializer = SalaPostSerializer(Miejsce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Sala = self.get_object(pk)
        Sala.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BiletList(APIView):
    permission_classes = [IsAuthenticated]  # Ustawianie klas zezwolen

    def get(self, request):
        bilet = Bilet.objects.all()
        serializer=BiletPostSerializer(bilet, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= BiletPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BiletDetail(APIView):
    permission_classes = [IsAuthenticated]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Bilet.objects.get(pk=pk)
        except Bilet.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Bilet = self.get_object(pk)
        serializer = BiletPostSerializer(Bilet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Bilet = self.get_object(pk)
        Bilet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ZamowienieList(APIView):
    permission_classes = [IsAuthenticated]  # Ustawianie klas zezwolen

    def get(self, request):
        bilet = Zamowienie.objects.all()
        serializer=ZamowieniePostSerializer(bilet, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= ZamowieniePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ZamowienieDetail(APIView):
    permission_classes = [IsAuthenticated]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Zamowienie.objects.get(pk=pk)
        except Zamowienie.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Zamowienie = self.get_object(pk)
        serializer = ZamowieniePostSerializer(Zamowienie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Zamowienie = self.get_object(pk)
        Zamowienie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UzytkownikList(APIView):
    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get(self, request):
        uzytkownik = Uzytkownik.objects.all()
        serializer=UzytkownikPostSerializer(uzytkownik, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= UzytkownikPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UzytkownikDetail(APIView):

    permission_classes = [IsAdminUser|ReadOnly]  # Ustawianie klas zezwolen

    def get_object(self, pk):
        try:
            return Uzytkownik.objects.get(pk=pk)
        except Uzytkownik.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Uzytkownik = self.get_object(pk)
        serializer = UzytkownikPostSerializer(Uzytkownik, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Uzytkownik = self.get_object(pk)
        Uzytkownik.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)