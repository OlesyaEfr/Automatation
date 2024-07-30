class Calculator:

    def sum(self, a, b):
        result = a+b
        return result
    
    def sub(self, a, b):
        result = a-b
        return result
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        if (b == 0): #проверка условий
            raise ArithmeticError("На ноль делить нельзя") #поднять ошибку
        return a/b #Возвращение результата деления
    
    def pow(self, a, b=2): #задали значение по умолчанию
        return a**b
    
    def avg(self, nums):
        if (len(nums) == 0):
            return 0
        s = 0
        for num in nums: #для каждого числа в списке
            s = s + num #вычисли переменную s, равную сумме s  и элемента списка
        
        l = len(nums)
        return self.div(s, l) #обратились к собственному методу класса