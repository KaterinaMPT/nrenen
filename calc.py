import math

def add(a,b):
  result = a + b
  return result
def diff(a,b):
  result = a - b
  return result
def delenie(a,b):
  result = a / b
  return result
def umnoj(a,b):
  result = a * b
  return result
def fact(a):
  if a > 0: 
    for i in range(1, a): a = a * i 
  elif a == 0:
    a = 1 
  return a
def sqrt(a):
  result = math.sqrt(a)
  return result
def sin(a):
  result =  math.sin(a)
  return result
def cos(a):
  result =  math.cos(a)
  return result
def tg(a):
  result =  math.tan(a)
  return result
def step(a,b):
  result =  a ** b
  return result
go = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить: ")
while go == "y":
    
    print("Доступные операции:")
    print("1. Сложение двух чисел", "2. Вычитание чисел", "3. Деление чисел", "4. Умножение чисел", "5. Факториал числа")
    print("6. Квадратный корень числа", "7. Нахождение синуса", "8. Нахождение косинуса", "9. Нахождение тангенса", "10. Возведение в степень")
    
    try:
       calc = input("Введите операцию: ")
    except(ValueError):
      print("Вы ввели не число")
      continue
       
    if calc == "5":  
       
     try:
      factorial = int(input())
      if factorial<0: 
        print("Не существует факториала отрицательного числа!")
      else:
        print(fact(factorial))
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "7":
      try:
        value = int(input("Введите число: "))
        print (sin(value))
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "9":
     try:
      value = int(input("Введите число: "))
      print (tg(value))
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "8":
     try:
      value = int(input("Введите число: "))
      print (cos(value))
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "6":
      try:
       value = int(input("Введите число: "))
       if value<0:
        print("Такой корень посчитать нельзя")
       else:
         print(sqrt(value))
      except(ValueError):
       print("Вы ввели не число")
       continue
       

    elif calc == "1":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(add(value1,value2))
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "2":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(diff(value1, value2))    
      except(ValueError):
        print("Вы ввели не число")
        continue

    elif calc == "4":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(umnoj(value1, value2))   
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "3":
       try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        if value2 != 0:
            print(delenie(value1,value2))
        else:
            print("На ноль делить нельзя!")    
       except(ValueError):
        print("Вы ввели не число")
        continue

    elif calc == "10":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(step(value1,value2))
      except(ValueError):
       print("Вы ввели не число")
       continue
      
    go = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить: ")
