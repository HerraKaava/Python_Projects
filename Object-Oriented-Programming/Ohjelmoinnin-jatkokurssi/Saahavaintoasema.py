

class Havaintoasema:
    # Konstruktori
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__havainnot = []

    def lisaa_havainto(self, havainto: str):
        self.__havainnot.append(havainto)

    def viimeisin_havainto(self):
        # if not self.__havainnot --> Jos havainnot-lista on TYHJÄ, niin tämä ehto on True --> enter the block
        if not self.__havainnot:
            return ""
        else:
            # Palautetaan listan viimeinen havainto
            return self.__havainnot[-1]

    def havaintojen_maara(self):
        return len(self.__havainnot)

    def __str__(self):
        return f"{self.__nimi}, {self.havaintojen_maara()} havaintoa"


if __name__ == "__main__":
    
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)

