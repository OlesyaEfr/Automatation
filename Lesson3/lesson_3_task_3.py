from address import Address
from mailing import Mailing

to_address = Address("151452", "Москва", "Ленина", "5", "55")
from_address = Address("412751", "Хвалынск", "К.Маркса", "1", "26")

mailing1 = Mailing(from_address, to_address, 1000, "56784123")

print("Отправление", mailing1.track, "из", mailing1.from_address.index, mailing1.from_address.city, mailing1.from_address.street, mailing1.from_address.home, "-", mailing1.from_address.flat, "в", mailing1.to_address.index, mailing1.to_address.city, mailing1.to_address.street, mailing1.to_address.home, "-", mailing1.to_address.flat, ".", "Стоимость", mailing1.cost, "рублей", ".")
