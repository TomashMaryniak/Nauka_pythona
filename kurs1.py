waga = int(input("Podaj swoj wage [kg]: "))
wzrost = int(input("Podaj wzrost [m]: "))
wiek = int(input("Podaj wiek [Lata]: "))
#plec = input("Plec [M, K]")
BMI = waga / (wzrost**2)
print("BMI:",BMI)
#if plec == M:
#    wspolczynnik = 5
#elif plec == K or k:
#    wspolczynnik = -161
#else :
#    Print("zly wybor plci")
kclM = ((10*waga)+(6.25*wzrost)-(5*wiek+5))
kclK = ((10*waga)+(6.25*wzrost)-(5*wiek-161))
print''
print'********************************************************'
print'********************************************************'
print''
print('Zapotrzebowanie kaloryczne na dla mezczyzn',kclM)
print('Zapotrzebowanie kaloryczne na dla mezczyzn',kclK)
