

class Lukutilasto:
    # Konstruktori
    def __init__(self):
        # Tyhjä lista, johon luvut lisätään
        self.lukuja = []


    def lisaa_luku(self, luku: int):
        self.luku = luku
        # Lisätään luvut konstruktorissa luotuun listaan
        self.lukuja.append(self.luku)


    # Metodi laskee listassa 'lukuja' olevien lukujen lukumäärän
    def lukujen_maara(self):
        return len(self.lukuja)


    # Metodi laskee listassa 'lukuja' olevien lukujen summan
    def summa(self):
        # Lasketaan lukujen summa
        return sum(self.lukuja)

    # Metodi laskee listassa 'lukuja' olevien lukujen keskiarvon
    def keskiarvo(self):
        if len(self.lukuja) > 0:
            keskiarvo = sum(self.lukuja) / len(self.lukuja)
            return keskiarvo
        else:
            return 0


# Luodaan ohjelma, joka kysyy lukuja käyttäjältä, kunnes käyttäjä syöttää luvun -1.
# Kun käyttäjä syöttää luvun -1, niin ohjelma ilmoittaa kaikkien lukujen summan, keskiarvon, \
# sekä parillisten ja parittomien lukujen summat erikseen.
# Toteutetaan ohjelma hyödyntäen luokkaa Lukutilasto.

# Luodaan kolme luokan Lukutilasto oliota ohjelmaa varten.
# Huomaa, että kun luodaan muuttuja, jonka tyyppi on yllä määritelty luokka Lukutilasto (kuten alla),
# niin muuttujalla on kaikki samat ominaisuudet, jotka on määritelty Lukutilasto-luokassa.
tilasto = Lukutilasto()       # <class '__main__.Lukutilasto'>
parilliset = Lukutilasto()    # <class '__main__.Lukutilasto'>
parittomat = Lukutilasto()    # <class '__main__.Lukutilasto'>

while True:
    # Pyydetään käyttäjää syöttämään jokin luku
    luku = int(input("Anna lukuja: \n"))

    # Jos käyttäjä syöttää luvun -1, niin ohjelma tulostaa yllä mainitut tilastot ja päättää ohjelma.
    if luku == -1:

        # Kaikkien lukujen summa
        print(f"Summa: {tilasto.summa()}")
        # Kaikkien lukujen keskiarvo
        print(f"Keskiarvo: {tilasto.keskiarvo()}")

        for num in tilasto.lukuja:
            if num % 2 == 0:    # Jos syötetty luku on parillinen, "annetaan" se parilliset-oliolle.
                parilliset.lisaa_luku(num)
            else:    # Jos syötetty luku on pariton, "annetaan" se parittomat-oliolle.
                parittomat.lisaa_luku(num)
        print(f"Parillisten summa: {parilliset.summa()}")
        print(f"Parittomien summa: {parittomat.summa()}")
        break

    # Tänne tullaan, jos käyttäjän syöttämä luku on mitä tahansa muuta kuin -1.
    # Tässä tapauksessa luku "annetaan" tilasto-oliolle.
    else:
        tilasto.lisaa_luku(luku)
