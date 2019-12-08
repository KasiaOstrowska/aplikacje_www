from rest_framework import serializers

class KinoPostSerializer(serializers.Serializer):
    nazwa=serializers.CharField(max_length=45)
    iloscSal=serializers.IntegerField()
    miejscowosc=serializers.CharField(max_length=45)

    def validate_nazwa(self,value):
       if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna nazwa",
            )
            return value

    def validate_iloscSal(self,value):
           if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Ilość sal musi być liczbą",
            )
            return value

    def validate_miejscowosc(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna nazwa miejscowości",
        )
        return value


class FilmPostSerializer(serializers.Serializer):
    tytul= serializers.TextField()
    rezyser= serializers.TextField()
    czas= serializers.FloatField()
    dataPremiert= serializers.DateField()

    def validate_tytul(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny tytuł",
        )
        return value

    def validate_rezyser(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błedny reżyser",
        )
        return value

    def validate_czas(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny czas",
        )
        return value

    def validate_dataPremierts(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna data",
        )
        return value

class SeansPostSerializer(serializers.Serializer):
    dataSeansu=serializers.DateTimeField()
    rodzajProjekcji=serializers.CharField(max_length=45)

    def validate_dataSeansu(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna data",
        )
        return value

    def validate_rodzajProjekcji(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny rodzaj",
        )
        return value

class SalaPostSerializer(serializers.Serializer):
    iloscMiejsc=serializers.IntegerField()
    numerSal=serializers.IntegerField()

    def validate_iloscMiejsc(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Ilość miejsc musi być liczbą",
        )
        return value

    def validate_numerSal(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny numer sali",
        )
        return value

class MiejscePostSerializer(serializers.Serializer):
    numerMiejsca=serializers.IntegerField()
    rzad=serializers.CharField(max_length=3)

    def validate_numerMiejsca(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Numer miejsca musi być liczbą",
        )
        return value

    def validate_rzad(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny rząd",
        )
        return value   

class BiletPostSerializer(serializers.Serializer):
    cenaJednostkowa=serializers.FloatField()
    rodzajBiletu=serializers.CharField(max_length=30)

    def validate_cenaJednostkowa(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna cena",
        )
        return value

    def validate_rodzajBiletu(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny rodzaj",
        )
        return value    

class ZamowieniePostSerializer(serializers.Serializer):
    cenaSprzedarzy=serializers.FloatField()
    dataZamowienia=serializers.DateField()
    status=serializers.CharField(max_length=20)

    def validate_cenaSprzedarzy(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błedny reżyser",
        )
        return value

    def validate_dataZamowienia(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędny czas",
        )
        return value

    def validate_status(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędna data",
        )
        return value

class UzytkownikPostSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=45)
    haslo=serializers.CharField(max_length=45)
    uprawnienia=serializers.CharField(max_length=50)
    imie=serializers.CharField(max_length=45)
    nazwisko=serializers.CharField(max_length=45)
    stanowisko=serializers.CharField(blank=True, null=True, max_length=45)

    def validate_email(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błedny e-mail",
        )
        return value

    def validate_haslo(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędne hasło",
        )
        return value

    def validate_uprawnienia(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędne uprawnienia",
        )
        return value
    def validate_imie(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błedne imie",
        )
        return value

    def validate_nazwisko(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędne nazwisko",
        )
        return value

    def validate_stanowisko(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Błędne stanowisko",
        )
        return value