

class Kello:

    # Konstruktori
    def __init__(self, tunnit, minuutit, sekunnit):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit


    def __str__(self):
        return f"{self.tunnit:02d}:{self.minuutit:02d}:{self.sekunnit:02d}"


    # Metodin kutsuminen lisää yhden sekunnin kelloon
    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:    # Jos sekunnit = 60, niin nollataan sekunnit ja kasvatetaan minuutteja yhdellä.
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:    # Jos minuutit = 60, niin nollataan minuutit ja kasvatetaan tunteja yhdellä.
                self.minuutit = 0
                self.tunnit += 1
                if self.tunnit == 24:    # Jos tunnit = 24, niin asetetaan tunnit nollaksi (digitaalinen kello)
                    self.tunnit = 0


    def aseta(self, tunnit, minuutit):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0


kello = Kello(23, 59, 55)
print(kello)    # 23:59:55
kello.tick()
kello.tick()
print(kello)    # 23:59:57
kello.aseta(12, 5)
print(kello)    # 12:05:00





