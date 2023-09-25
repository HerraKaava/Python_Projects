

import random

class Sanapeli:
    def __init__(self, kierrokset: int):
        self.voitot1 = 0    # Pelaajan 1 voittojen lukumäärä
        self.voitot2 = 0    # Pelaajan 2 voittojen lukumäärä
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)     # randint()-funktio arpoo luvun suljetulta väliltä [a, b]

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass    # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")


# Luokka PisinSana perii luokan Sanapeli.
# Tässä pelin versiossa kunkin kierroksen voittaja on sen kierroksen aikana pidemmän sanan syöttänyt käyttäjä.
class PisinSana(Sanapeli):
    # Konstruktori (peritään yliluokalta)
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    # Ylikirjoitetaan yliluokan metodi kierroksen_voittaja() siten,
    # että em. käytännöllisyys toteutuu (pisin sana voittaa).
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):

        # Jos pelaajan 1 sana on pidempi, palautetaan 1 (jolloin pelaa metodissa pelaaja 1 asetetaan voittajaksi).
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1

        # Jos pelaajan 2 sana on pidempi, palautetaan 2 (jolloin pelaa metodissa pelaaja 2 asetetaan voittajaksi).
        elif len(pelaaja2_sana) > len(pelaaja1_sana):
            return 2

        # Muutoin (eli jos sanat ovat yhtä pitkät) annetaan pass -avainsana.
        # Pythonissa pass on nk. paikanvaraaja (engl. placeholder) statement, joka ei tee MITÄÄN.
        # Sitä käytetään silloin, kun statement vaaditaan syntaktisesti,
        # mutta ei haluta mitään koodia tai toimintoja.
        # Tässä siis käytetään pass -paikanvaraajaa siten, että mikäli pelaajien 1 ja 2 sanat ovat yhtä pitkiä,
        # niin mitään toimintoja ei tarvita, vaan seuraava kierros käynnistyy normaalisti
        # (next line of code is executed).
        else:
            pass    # tasapeli


# Luokka EnitenVokaaleja perii luokan Sanapeli.
# Tässä pelin versiossa kunkin kierroksen voittaja on se pelaaja, jonka sanassa on enemmän vokaaleja.
class EnitenVokaaleja(Sanapeli):
    # Konstruktori (peritään yliluokalta)
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # Alustetaan vokaalit listaan,
        # ja tehdään kaksi apumuuttujaa, joilla pidetään kirjaa pelaajien 1 ja 2 sanojen vokaaleista.
        vokaalit = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
        pelaajan1_vokaalit = 0
        pelaajan2_vokaalit = 0

        for kirjain in pelaaja1_sana:
            if kirjain in vokaalit:
                pelaajan1_vokaalit += 1

        for kirjain in pelaaja2_sana:
            if kirjain in vokaalit:
                pelaajan2_vokaalit += 1

        if pelaajan1_vokaalit > pelaajan2_vokaalit:
            return 1
        elif pelaajan2_vokaalit > pelaajan1_vokaalit:
            return 2
        else:
            pass


# Tämä luokka mallintaa nimensä mukaisesti kivi, paperi ja sakset -peliä.
class KiviPaperiSakset(Sanapeli):
    # Konstruktori (peritään yliluokalta)
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # Alustetaan pelissä käytettävät välineet listaan
        valineet = ["kivi", "paperi", "sakset"]

        # Pelaajan 1 kaikki voittotavat
        if pelaaja1_sana == valineet[0] and pelaaja2_sana == valineet[2]:
            return 1
        elif pelaaja1_sana == valineet[1] and pelaaja2_sana == valineet[0]:
            return 1
        elif pelaaja1_sana == valineet[2] and pelaaja2_sana == valineet[1]:
            return 1

        # Pelaajan 2 kaikki voittotavat
        if pelaaja2_sana == valineet[0] and pelaaja1_sana == valineet[2]:
            return 2
        elif pelaaja2_sana == valineet[1] and pelaaja1_sana == valineet[0]:
            return 2
        elif pelaaja2_sana == valineet[2] and pelaaja1_sana == valineet[1]:
            return 2

        # Tasurit
        if pelaaja2_sana == valineet[0] and pelaaja1_sana == valineet[0]:
            pass
        elif pelaaja2_sana == valineet[1] and pelaaja1_sana == valineet[1]:
            pass
        elif pelaaja2_sana == valineet[2] and pelaaja1_sana == valineet[2]:
            pass

        # Jos pelaajan syöte on epäkelpo, eli se ei ole mikään sanoista kivi, paperi tai sakset,
        # pelaaja häviää kierroksen, ellei molempien syöte ole epäkelpo.

        # Jos pelaajan 1 sana on epäkelpo, pelaaja 2 voittaa.
        if pelaaja1_sana not in valineet and pelaaja2_sana in valineet:
            return 2

        # Jos pelaajan 2 sana on epäkelpo, pelaaja 1 voittaa
        if pelaaja2_sana not in valineet and pelaaja1_sana in valineet:
            return 1

        # Jos molempien pelaajien sanat ovat epäkelvot --> pass
        if pelaaja2_sana not in valineet and pelaaja1_sana not in valineet:
            pass


if __name__ == "__main__":
    p = KiviPaperiSakset(4)
    p.pelaa()

