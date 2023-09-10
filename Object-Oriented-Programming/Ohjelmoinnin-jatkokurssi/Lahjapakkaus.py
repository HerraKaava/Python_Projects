

class Lahja:
    # Konstruktori
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"


class Pakkaus:
    # Konstruktori.
    def __init__(self):
        self.lahjapakkaus = []


    # Tämä metodi lisää lahjapakkaus-listaan parametrina syötetyn lahjan.
    # (Huomaa, että metodin parametri on luokan Lahja olio).
    def lisaa_lahja(self, lahja: Lahja):
        self.lahjapakkaus.append(lahja)


    # Tämä metodi laskee lahjapakkauksessa olevien lahjojen yhteispainon
    def yhteispaino(self):
        total_weight = []    # Luodaan tyhjä lista, johon lisätään lahjojen painot

        # Täsäs silmukassa käydään läpi lahjapakkaus-lista (joka sisältää luokan Lahja olioita),
        # ja lisätään kunkin olion (lahjan) paino total_weight-listaan.
        for lahja in self.lahjapakkaus:
            total_weight.append(lahja.paino)

        return sum(total_weight)


if __name__ == "__main__":

    kirja = Lahja("Aapiskukko", 2)
    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())

    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())

