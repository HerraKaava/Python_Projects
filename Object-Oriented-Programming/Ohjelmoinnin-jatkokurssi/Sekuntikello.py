

class Sekuntikello:
    # Konstruktori
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0


    def __str__(self):
        # Katso tämän muotoilun selitys alta
        return f"{self.minuutit:02d}:{self.sekunnit:02d}"


    def tick(self):
        self.sekunnit += 1    # Aina kun 'tick' -metodia kutsutaan, kelloon lisätään 1 sekunti.
        if self.sekunnit == 60:    # Kun sekunnit = 60, nollataan sekunnit ja kasvatetaan minuutteja yhdellä.
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0


kello = Sekuntikello()

# Suoritetaan 3600 iterointikierrosta, jolloin kello kulkee nollasta 59:59 asti.
for i in range(3600):
    print(kello)
    kello.tick()


# In the expression f"{self.minuutit:02d}", the :02d is a formatting specifier called a format specifier.
# It is used to format the value of self.minuutit as a string with a width of 2 characters,
# filled with leading zeros if necessary.

# Breaking it down:

#   - ":" indicates the start of the format specifier.
#   - "0" specifies that leading zeros should be used for filling.
#   - "d" indicates that the value being formatted is a decimal integer.
