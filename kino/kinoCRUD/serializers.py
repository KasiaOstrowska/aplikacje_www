from rest_framework import serializers
from .models import *
class KinoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Kino
        fields ='__all__'

class FilmPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields ='__all__'

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

class SalaPostSerializer(serializers.ModelSerializer):
   class Meta:
        model = Sala
        fields = '__all__'

class MiejscePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miejsce
        fields ='__all__'   

class BiletPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilet
        fields=('cenaJednostkowa', 'rodzajBiletu', 'idSeans', 'idMiejsca')
    
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

class ZamowieniePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields ='__all__' 

    # def validate_cenaSprzedarzy(self,value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError(
    #             "Błedna cena",
    #     )
    #     return value

    # def validate_dataZamowienia(self,data):
    #     if data['dataZamowienia'] > data['now']:
    #         raise serializers.ValidationError(
    #             "Błędny czas",
    #     )
    #     return value

    # def validate_status(self,value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError(
    #             "Błędna data",
    #     )
    #     return value

class UzytkownikPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Uzytkownik
        fields ='__all__'

    # # def validate_email(self,value):
    # #     if 'django' not in value.lower():
    # #         raise serializers.ValidationError(
    # #             "Błedny e-mail",
    # #     )
    # #     return value

    # # def validate_haslo(self,value):
    # #     if 'django' not in value.lower():
    # #         raise serializers.ValidationError(
    # #             "Błędne hasło",
    # #     )
    # #     return value

    # def validate_uprawnienia(self,value):
    #     if 'django' not in ("Klient", "Admin"):
    #         raise serializers.ValidationError(
    #             "Błędne uprawnienia",
    #     )
    #     return value
    # # def validate_imie(self,value):
    # #     if 'django' not in value.lower():
    # #         raise serializers.ValidationError(
    # #             "Błedne imie",
    # #     )
    # #     return value

    # def validate_nazwisko(self,value):
    #     if 'django' not in ("Klient", "Admin"):
    #         raise serializers.ValidationError(
    #             "Błędne nazwisko",
    #     )
    #     return value
