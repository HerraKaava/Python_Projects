

class Auto:
    # Konstruktori
    def __init__(self):
        # Note that the two underscores before the attributes are used to make them private.
        # This means that they are intended to be accessed and modified only from within the class itself,
        # and that they are not meant to be directly accessed or modified from outside the class.
        self.__tankki = 0
        self.__ajettu = 0


    def __str__(self):
        return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__tankki} litraa"


    def tankkaa(self):
        self.__tankki = 60


    def aja(self, km: int):
        if km > self.__tankki:
            self.__ajettu += self.__tankki
            self.__tankki = 0
        else:
            self.__ajettu += km
            self.__tankki -= km


if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)





