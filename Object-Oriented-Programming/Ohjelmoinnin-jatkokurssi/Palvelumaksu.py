

class Pankkitili:
    # Konstruktori.
    # Huomaa, että kaikki attribuutit ovat piilotettuja.
    def __init__(self, tilinomistaja: str, tilinumero: str, saldo: float):
        self.__tilinomistaja = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo

    def talleta(self, summa: float):
        self.__saldo += summa
        # Kutsutaan yksityistä metodia __palvelumaksu talletuksen yhteydessä,
        # jotta tililtä menee 1 %:n palvelumaksu
        self.__palvelumaksu()

    def nosta(self, summa: float):
        self.__saldo -= summa
        # Kutsutaan yksityistä metodia __palvelumaksu noston yhteydessä,
        # jotta tililtä menee 1 %:n palvelumaksu
        self.__palvelumaksu()

    # Havainnointimetodi
    @property
    def saldo(self):
        return self.__saldo

    # Yksityinen metodi
    def __palvelumaksu(self):
        # Palvelumaksu on 1 % eli tililtä vähennetään 1 % (saldosta) talletuksen tai noston yhteydessä
        self.__saldo = self.__saldo * 0.99


if __name__ == "__main__":

    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)
