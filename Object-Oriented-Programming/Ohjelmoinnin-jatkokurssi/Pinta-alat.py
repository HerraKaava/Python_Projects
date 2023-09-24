

class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    # Suorakulmion pinta-ala on kanta (leveys) * korkeus.
    def pinta_ala(self):
        return self.leveys * self.korkeus


# Luokka Nelio perii luokan Suorakulmio.
class Nelio(Suorakulmio):
    # super() -funktion avulla viitataan yliluokan (parent class) konstruktoriin.
    # Huomaa, että yliluokan konstruktorista peritään ainoastaan yksi parametri (ihan sama kumpi).
    # However, koska yliluokassa on kaksi parametria, täytyy myös alaluokan viittauksessa olla kaksi parametria.
    # Tässä voidaan menetellä niin, että annetaan sama parametri kahdesti super()-funktion jälkeisessä konstruktorissa.
    def __init__(self, leveys: int):
        super().__init__(leveys, leveys)

    def pinta_ala(self):
        return self.leveys * self.leveys

    def __str__(self):
        return f"neliö {self.leveys}x{self.korkeus}"


if __name__ == "__main__":

    nelio = Nelio(4)
    print(nelio)        # neliö 4x4
    print("pinta-ala:", nelio.pinta_ala())      # pinta-ala: 16
