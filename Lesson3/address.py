class Address:

    def __init__(self, index, city, street, home, flat):
        self.i = index
        self.c = city
        self.s = street
        self.h = home
        self.f = flat

    def addressPrint(self):
        print(self.i, self.c, self.s, self.h, "-", self.f)