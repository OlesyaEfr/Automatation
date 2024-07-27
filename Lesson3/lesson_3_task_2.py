from smartphone import Smartphone

smartphone1 = Smartphone("Apple", "15Pro", "79779777779")
smartphone2 = Smartphone("Samsung", "GalaxyS24", "79997779999")
smartphone3 = Smartphone("Sony", "xperia10", "77779997799")
smartphone4 = Smartphone("Xiaomi", "Redmi13C", "79011112233")
smartphone5 = Smartphone("Honor", "X9b", "79011112345")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for smartphones in catalog:
    smartphones.inf()
