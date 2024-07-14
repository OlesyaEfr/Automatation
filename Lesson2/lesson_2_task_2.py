year_as_string = input("Введите год: ")
year = int(year_as_string)

def is_year_leap():
       if (year % 4 == 0):
          print("Год", year,":", "True")
       else:
           print("Год", year,":", "False")
is_year_leap()