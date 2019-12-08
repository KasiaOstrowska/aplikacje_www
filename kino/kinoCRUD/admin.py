from django.contrib import admin

# Register your models here.
from .models import Seans
from .models import Kino
from .models import Film
from .models import Bilet
from .models import Miejsce
from .models import Sala
from .models import Uzytkownik
from .models import Zamowienie

admin.site.register(Seans)
admin.site.register(Kino)
admin.site.register(Film)
admin.site.register(Bilet)
admin.site.register(Miejsce)
admin.site.register(Sala)
admin.site.register(Uzytkownik)
admin.site.register(Zamowienie)

