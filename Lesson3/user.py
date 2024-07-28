class User:
     
    def __init__(self, first_name, last_name):
        self.Username = first_name
        self.Usersurname = last_name
    
    def sayName(self):
        print(self.Username)

    def saySurname(self):
        print(self.Usersurname)

    def NameSurname(self):
        print(self.Username, self.Usersurname)

