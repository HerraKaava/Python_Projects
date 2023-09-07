

class Kirja:

    # Konstruktori
    def __init__(self, nimi, kirjoittaja, genre, kirjoitusvuosi):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

def genren_kirjat(kirjat, genre):
    """
    Funktio luo uuden listan sille syötetystä listasta siten,
    että uusi lista sisältää ainoastaan oikean genren kirjat.

    Args:
        kirjat (list): Lista luokan Kirja olioita.
        genre (str): Kertoo luokan Kirja olion genren.

    Returns:
        Funktio palauttaa uuden listan, jolle se tallentaa parametrina olevista kirjoista ne,
        joilla on haluttu genre.
    """
    uusi_lista = []
    for kirja in kirjat:
        if kirja.genre == genre:
            uusi_lista.append(kirja)

    return uusi_lista


python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)
Lumiukko = Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)

kirjat = [python, everest, norma, Lumiukko]

print("rikoskirjoja ovat")
for kirja in genren_kirjat(kirjat, "rikos"):
    print(f"{kirja.kirjoittaja}: {kirja.nimi}")