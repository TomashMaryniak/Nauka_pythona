# -*- coding: utf-8 -*-
waga = int(input("Podaj swoj wage [kg]: "))
wzrost = int(input("Podaj wzrost [cm]: "))
wiek = int(input("Podaj wiek [Lata]: "))
plec = raw_input("Plec [M, K]")
if plec == "M" or "m":
    wspolczynnik = 5
elif plec == "K" or "k":
    wspolczynnik = -161
else :
    Print("zly wybor plci")
print("Jak ocenasz swoja aktywnosc od [1-5]\n")
wysilek = int(input("Gdzie 1 to brak aktywnosci ,5 to aktywnosc B-duza \n"))
if wysilek == 1:
    sila = 1.2
elif wysilek == 2:
    sila = 1.4
elif wysilek == 3:
    sila = 1.6
elif wysilek == 4:
    sila = 1.4
elif wysilek == 5:
    sila = 1.6
# else print("kupa")
kcl = (10*waga)+(6.25*wzrost)-(5*wiek)+(wspolczynnik)
wzrostm = wzrost / 100
print('Zapotrzebowanie kaloryczne wynosi',kcl*sila)
BMI = waga / wzrostm ** 2
print("A BMI wynosi :",BMI)
