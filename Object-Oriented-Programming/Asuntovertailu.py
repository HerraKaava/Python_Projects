

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    # Huomaa, että tyyppivihje pitää antaa hipsuissa, jos parametri on saman luokan olio!
    def suurempi(self, verrattava: "Asunto"):
        if self.nelioita > verrattava.nelioita:
            return True
        else:
            return False

    def hintaero(self, verrattava: "Asunto"):
        # Metodi palauttaa asunto-olion ja verrattavan asunto-olion hintaeron.
        # Hintaero on asuntojen hintojen erotuksen itseisarvo (hinta on neliöt * neliöhinta).
        return abs(self.nelioita * self.neliohinta - verrattava.nelioita * verrattava.neliohinta)

    def kalliimpi(self, verrattava: "Asunto"):
        if (self.nelioita * self.neliohinta) > (verrattava.nelioita * verrattava.neliohinta):
            return True
        else:
            return False


