print("Kalkulator stanu konta")
stan_poczatkowy = int(input("Podaj stan poczatkowy konta "))
oprocent_roczne = int(input("podaj oprocentowanie roczne "))
lata_lokaty = int(input("Ile lat na lokacie "))
print("Stan konta po {} latach z wplata startowa {} z oprocentoaniem {}".format(lata_lokaty,stan_poczatkowy,oprocent_roczne))
miesiace = lata_lokaty * 12
stan_poczatkowy*(1 + lata_lokaty * (oprocent_roczne/100) )

print("bedzie wynosic {} " .format(saldo))
