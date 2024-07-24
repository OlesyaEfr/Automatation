from address import Address
from mailing import Mailing

to_address = Address("151452", "Москва", "Ленина", "5", "55")
to_address.addressPrint()
from_address = Address("412751", "Хвалынск", "К.Маркса", "1", "26")
from_address.addressPrint()

mailing1 = Mailing(from_address, to_address, 1000, "5897654" )
#mailing1.mail()
print("Отправление", mailing1.track, "из", from_address, "в", to_address, ".", "Стоимость", mailing1.cost, "рублей.")