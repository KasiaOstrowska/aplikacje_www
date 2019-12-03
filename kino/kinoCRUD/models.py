from django.db import models

# Create your models here.
class Kino(models.Model):
    nazwa=models.CharField(max_length=45)
    iloscSal=models.IntegerField()
    miejscowosc=models.CharField(max_length=45)


class Film(models.Model):
    tytul= models.TextField()
    rezyser= models.TextField()
    czas= models.FloatField()
    dataPremiert= models.DateField()

class Seans(models.Model):
    dataSeansu=models.DateTimeField()
    rodzajProjekcji=models.CharField(max_length=45)
    idFilm=models.ForeignKey('Film',on_delete=models.CASCADE)
    idSala=models.ForeignKey('Sala', on_delete=models.CASCADE)

class Sala(models.Model):
    iloscMiejsc=models.IntegerField()
    numerSal=models.IntegerField()
    idKino=models.ForeignKey('Kino', on_delete=models.CASCADE)

class Miejsce(models.Model):
    numerMiejsca=models.IntegerField()
    rzad=models.CharField(max_length=3)
    idSala=models.ForeignKey('Sala', on_delete=models.CASCADE)

class Bilet(models.Model):
    idMiejsca=models.ForeignKey('Miejsce', on_delete=models.CASCADE)
    cenaJednostkowa=models.FloatField()
    rodzajBiletu=models.CharField(max_length=30)
    idSeans=models.ForeignKey('Seans', on_delete=models.CASCADE)

class Zamowienie(models.Model):
    cenaSprzedarzy=models.FloatField()
    dataZamowienia=models.DateField()
    status=models.CharField(max_length=20)
    idKlient=models.ForeignKey('Uzytkownik', on_delete=models.PROTECT)

class ZamowieniBilet(models.Model):
    idBilet=models.ForeignKey('Bilet', on_delete=models.CASCADE)
    idZamowinie=models.ForeignKey('Zamowienie', on_delete=models.CASCADE)

class Uzytkownik(models.Model):
    email=models.CharField(max_length=45)
    haslo=models.CharField(max_length=45)
    uprawnienia=models.CharField(max_length=50)
    imie=models.CharField(max_length=45)
    nazwisko=models.CharField(max_length=45)
    stanowisko=models.CharField(blank=True, null=True, max_length=45)

class KinoUser(models.Model):
    idKino=models.ForeignKey('Kino', on_delete=models.PROTECT)
    idUser=models.ForeignKey('Uzytkownik', on_delete=models.CASCADE)    
