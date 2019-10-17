def return_list(a_list, b_list):
    lista = []
    for i in range(0, len(a_list),2):
        lista.append(a_list[i])
    for i in range(1, len(b_list),2):
        lista.append(b_list[i])
    return lista


def return_dict(data_text):
    length = len(data_text)
    letter= []
    for char in data_text:
        letter.append(char)
    big_letters=data_text.upper()
    small_letters= data_text.lower()
    letters= set(letter)
    dictionary = dict({"length": length, "letters":letters, "big_letters": big_letters, "small_letters": small_letters})
    return dictionary


def remove(text, letter):
    for l in letter:
        text=text.replace(l, "")
    return text


def temperature_calc(temperature, temperature_type):
    if temperature_type == '1':
        temp= (float(temperature) * 1.8)+32
    elif temperature_type == '2':
        temp = float(temperature) + 237.15
    elif temperature_type == '3':
        temp=(float(temperature)+237.15)*1.8
    else:
        temp="Podales bledna wartosc"
    return temp

def replace(text):
    replace_text=""
    for i in range(len(text)-1, -1,-1):
        replace_text=replace_text +text[i]
    return replace_text


class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def difference(self, a,b):
        return a-b

    def multiply(self, a,b):
        if a==0:
            return 'error: multiplied by zero'
        elif b==0:
            return 'error: multiplied by zero'
        return a*b

    def divide(self, a,b):
        if b==0:
            return 'error: division by zero'
        return a/b


class ScienceCalculator(Calculator):
    def __init__(self):
        pass
    def power(self,a):
        return a*a

#Zadanie 1
a_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    ]
b_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    ]
print(return_list(a_list,b_list))
#Zadanie 2
text='DogD'
print(return_dict(text))
#Zadanie 3
text = 'Znaki do usuniecia: x, z, g, f, G, H'
letter = ',xzgfGH'
print(remove(text,letter))
#Zadanie 4
print('Podaj temperature')
temper=input()
print('Podaj typ konwersji')
print('1 - Fahrenheit')
print('2- Kelvin')
print('3- Rankine')
temperature_type=input()
print(temperature_calc(float(temper), temperature_type))
# Zadanie 5
calc=Calculator()
print(calc.add(2,3))
print(calc.difference(2,3))
print(calc.multiply(2,3))
print(calc.divide(2,3))
# Zadanie 6
calculator = ScienceCalculator()
print( calculator.power(12))
#Zadanie 7
print(replace(text))
#Zadanie 8
input()
