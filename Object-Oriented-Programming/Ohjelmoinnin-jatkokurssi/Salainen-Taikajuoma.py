

class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi       # Suojattu attribuutti
        self._ainekset = []     # Suojattu attribuutti

        # Yhdellä alaviivalla alkavat piirteet ovat tarkoitettu ainoastaan luokan ja sen aliluokkien käyttöön,
        # eikä niitä tulisi käyttää suoraan näiden ulkopuolelta (tämä on yleinen konventio Python-yhteisössä).

    def lisaa_aines(self, ainesosa: str, maara: float):
        # Lisätään aines tuplen muodossa
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")


# SalainenTaikajuoma-luokka perii Taikajuoma-luokan.
class SalainenTaikajuoma(Taikajuoma):
    # Konstruktori (huomaa, että nimi-parametri peritään Taikajuoma-yliluokalta,
    # mutta salasana on tämän aliluokan oma parametri).
    def __init__(self, nimi: str, salasana: str):
        super().__init__(nimi)
        self.salasana = salasana

    # Jos metodeja kutsutaan väärällä salasanalla, ne antavat ValueError-poikkeuksen.
    # Jos salasana on oikein, kutsutaan perityn luokan Taikajuoma vastaavaa metodia.
    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        if salasana != self.salasana:
            raise ValueError("Väärä salasana!")
        else:
            # Muista, että viitatessa perityn luokan metodiin, täytyy käyttää super() -funktiota!
            super().lisaa_aines(ainesosa, maara)

    def tulosta_resepti(self, salasana: str):
        if salasana != self.salasana:
            raise ValueError("Väärä salasana!")
        else:
            super().tulosta_resepti()


if __name__ == "__main__":
    
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "hokkuspokkus")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
    kutistus.tulosta_resepti("hokkuspokkus")

    kutistus.tulosta_resepti("pokkushokkus")    # ValueError: Väärä salasana!


