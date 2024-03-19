from enum import IntEnum

def dodawanie_definicji(definicje, klucz, definicja):
    definicje[klucz] = definicja
    print(" Definicja ", definicje[klucz], " została dodana. ")

def wyszukiwanie_definijci(definicje, klucz):
    if klucz in definicje:
        print(" Twoje słowo, ", klucz, " znajduje sie w bazie.")
    else:
        print(" Twoje słowo", klucz, "nie znajduje się w bazie.")

def usuwanie_definijci(definicje, klucz):
    if klucz in definicje:
        del definicje[klucz]
        print(" Twoja definicja ", definicje[klucz], " została usunięta z bazy. ")
    else: 
        print(" Nie odnaleziono słowa", klucz, "w bazie. ")

print(" Napiszesz program, który będzie wirtualnym słownikiem ")
print("n/")

definicje = { }
Menu_funkcji = IntEnum('Menu_funkcji', [' Dodanie ', ' Usuwanie ', ' Wyszukiwanie ', ' Zakończenie '])

while(True):

    print(" Wybierz co chcesz zrobić: ")
    print(" 1 - jeżeli chcesz dodać definicję")
    print(" 2 - jeżeli chcesz wyszukać definicję w słowniku")
    print(" 3 - jeżeli chcesz usunąć definicję ze słownika")
    print(" 4 - jeżeli chcesz zakończyć program")

    wybor = int(input(" Twój wybór to: "))

    if wybor == Menu_funkcji. Dodanie:
        print(" Wybrałeś dodawanie definicji ") 
        klucz = str(input(" Wrowadź słowo: "))
        definicja = str(input(" Wprowadź definicję: "))
        dodawanie_definicji(definicje, klucz, definicja)
    
    if wybor == Menu_funkcji.Usuwanie:
        print(" WYbrałeś usuwanie definicji ze słownika.")
        klucz = str(input(" Podaj słowo, które ma zostać usunięte: "))
        usuwanie_definijci(definicje, klucz)

    if wybor == Menu_funkcji.Wyszukiwanie:
        print(" WYbrałeś wyszukiwanie definicji w słowniku.")
        klucz = str(input(" Podaj słowo, które ma zostać wyszukane: "))
        usuwanie_definijci(definicje, klucz)
    
    if wybor == Menu_funkcji.Zakończenie:
        print(" Wybrano zakończenie programu ")
        break
