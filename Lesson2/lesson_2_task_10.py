def bank(x, y):
    percent = 0.10
    sum_after_y_years = x * (1 + percent) ** y
    return sum_after_y_years

x = float(input("Какая сумма вклада? "))
y = int(input("На сколько лет вклад? "))

result = bank(x, y)
print("Итоговая сумма для получения через ", y, "лет", "составляет", result)