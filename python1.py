from datetime import datetime
#Zadanie 1
zmienna_lorem_ipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.' 
zmienna_lorem_ipsum=zmienna_lorem_ipsum+'Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki.' 
zmienna_lorem_ipsum=zmienna_lorem_ipsum+'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym.'
zmienna_lorem_ipsum=zmienna_lorem_ipsum+'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum'
zmienna_lorem_ipsum=zmienna_lorem_ipsum+', a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na '
zmienna_lorem_ipsum=zmienna_lorem_ipsum+'komputerach osobistych, jak Aldus PageMaker'
print(zmienna_lorem_ipsum)
input()
#Zadanie 2
imie="Katarzyna"
nazwisko='Ostrowska'
print('W tekscie jest %i liter %s oraz %i liter %s' % (zmienna_lorem_ipsum.count(imie[2]), imie[2],zmienna_lorem_ipsum.count(nazwisko[3]),nazwisko[3]))
input()
#Zadanie 3
New= 'new'
print('{:^100}'.format(New))
print('{:.{prec}} = {:.{prec}f}'.format('New', 2.71235568746182, prec=7))

print('{:{dfmt} {tfmt}}'.format(datetime(2019,10,17,12,22), dfmt='%Y-%m-%d', tfmt='%H:%M'))
input()
#Zadanie 4
print(dir(zmienna_lorem_ipsum))
help(zmienna_lorem_ipsum.format)
input()
#Zadanie 6 
lista10 = [
	1, 2, 3,
	4, 5, 6,
	7, 8, 9,
	10,
	]
print('Lista poczatkowa ')
print(lista10)
newlist = [
	lista10.pop(9),lista10.pop(8),lista10.pop(7),
	lista10.pop(6),lista10.pop(5),
	]
newlist.sort()
print('Nowa lista ')
print(newlist)
print('Stara lista ')
print(lista10)
input()
#Zadanie 7
lista10.insert(0,0)
for x in newlist:
    lista10.append(x)
print('Sklejona lista ')
print(lista10)
print('Odwrócona kopia ')
lista=lista10
print(lista10.reverse())
#zwraca none
input()
#Zadanie 8
student1= (144102, 'Katarzyna','Ostrowska')
student2= (121212, 'Maksymilian','Pliszczyński')
student3= (141414, 'Dominika','Gala')
student4= (151515, 'Jakub', 'Lis')
studenci= [
	student1, student2,
	student3, student4,
	]
print(studenci)
input()
#Zadanie 9 
słownik={}
# tworzenie słownika
slownik = {}
for student in studenci:
	slownik[student[0]]=student[1:3] 

# wypisanie wszystkich kluczy
print(slownik.keys())

# wypisanie wszystkich wartości
print(slownik.values())
print(słownik)
input()
#Zadanie 10
numery_z_powtorzeniami= [
	'123456789', '234567890', '345678901',
	'432109876', '321098765', '123456789',
	'345678901', '432109876',
	]
numery_bez_powtorzen= set(numery_z_powtorzeniami)
print(numery_z_powtorzeniami)
print(numery_bez_powtorzen)
input()
#Zadanie 11
for i in range(1,11):
	print(i)
input()
#Zadanie 12
for i in range(100, 19, -5):
	print(i)
input()
#Zadanie 13
lista_slownikow=[
	]
