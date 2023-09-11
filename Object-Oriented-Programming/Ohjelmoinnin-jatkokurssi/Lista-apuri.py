

# Luokkametodi eli staattinen metodi on luokassa oleva metodi,
# jota ei ole sidottu mihinkään luokasta muodostettuun olioon.
# Niinpä luokkametodia voi kutsua ilman, että luokasta muodostetaan oliota.

# Luokkametodi merkitään annotaatiolla @classmethod ja sen ensimmäinen parametri on aina cls.
# Tunnistetta cls käytetään samaan tapaan kuin tunnistetta self,
# mutta erotuksena on, että cls viittaa luokkaan ja self viittaa olioon.
# Kummallekaan parametrille ei anneta kutsuessa arvoa, vaan Python tekee sen automaattisesti

class ListaApuri:

    @classmethod
    # Tämä metodi palauttaa alkion, joka esiintyy parametrina annetussa listassa useiten.
    def suurin_frekvenssi(cls, lista: list):
        d = {}
        for num in lista:
            # Jos iterointivuorossa oleva numero ei ole vielä avaimena sanakirjassa d,
            # niin lisätään se avaimeksi ja alustetaan sen arvo ykköseksi (koska tämä oli sen 1. esiintymiskerta).
            if num not in d:
                d[num] = 1
            # Muutoin kasvatetaan iterointivuorossa olevan avaimen arvoa ykkösellä.
            else:
                d[num] += 1
        # Palautetaan sanakirjasta d se avain, jolla on suurin arvo.
        return max(d, key=d.get)


    @classmethod
    # Tämä metodi palauttaa sellaisten alkioiden lukumäärän, jotka esiintyvät listassa vähintään kahdesti.
    def tuplia(cls, lista: list):
        d = {}
        for num in lista:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        numerot = []
        for key, value in d.items():
            if value >= 2:
                numerot.append(key)

        # Palautetaan 'numerot' listan pituus eli tieto siitä,
        # kuinka monta eri numeroa esiintyy listassa vähintään kahdesti
        # (tässä listassa on siis ne alkiot, jotka esiintyvät parametrina annetussa listassa vähintään kahdesti).
        return len(numerot)


if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))


###### get() -metodi #####

# get() method is a built-in method that allows you to retrieve the value associated with a given key.
# It has the following syntax: dictionary.get(key, default). Here's what each parameter means:

    # key: The key whose associated value you want to retrieve from the dictionary.

    # default (optional): The value to return if the specified key is not found in the dictionary.
    # If not provided, it defaults to None.


# Esimerkki 1.

x = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8]
d = {}
for val in x:
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1

print(d)

# Yhdessä max() -funktion kanssa, kun määritetään key=d.get, palautetaan se sanakirjan d AVAIN,
# jolla on suurin arvo (tässä tapauksessa siis se luku, joka esiintyy listassa useiten).
print(max(d, key=d.get))


# Esimerkki 2.

# Tämä koodi palauttaa sanakirjan d avaimen 1 arvon.
print(d.get(1))


# Esimerkki 3.

# get() -metodille voidaan antaa vakioarvo, joka palautetaan, mikäli haettavaa avainta ei löydy sanakirjasta.
print(d.get(10, "Sanakirjassa ei ole kymppiä!"))