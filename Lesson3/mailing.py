from address import Address

class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to = to_address
        self.from_ = from_address
        self.cost = cost
        self.track = track

    #def mail(self):
        #print("Отправление", self.track, "из", self.from_, "в", self.to, ".", "Стоимость", self.cost, "рублей.")
        

 