import math

loop = "y"

   
while loop == "y":
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
      factorial = int(input("Введите число: ")) 
      if factorial > 0: 
       for i in range(1, factorial): factorial = factorial * i 
       print(factorial) 
      elif factorial == 0:
       factorial = 1 
       print(factorial)
      else: 
       print("Не существует факториала отрицательного числа!")
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "7":
      try:
        value = int(input("Введите число: "))
        print (("синус числа = "), math.sin(value))
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "9":
     try:
      value = int(input("Введите число: "))
      print (("тангенс числа = "), math.tan(value))
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "8":
     try:
      value = int(input("Введите число: "))
      print (("косинус числа = "), math.cos(value))
     except(ValueError):
      print("Вы ввели не число")
      continue

    elif calc == "6":
      try:
       value = int(input("Введите число: "))
       if value >= 1:
        print (("квадратный корень числа = "), math.sqrt(value))
       else:
        print("Такой корень посчитать нельзя")
      except(ValueError):
       print("Вы ввели не число")
       continue
       

    elif calc == "1":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 + value2)
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "2":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 - value2)    
      except(ValueError):
        print("Вы ввели не число")
        continue

    elif calc == "4":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 * value2)   
      except(ValueError):
       print("Вы ввели не число")
       continue

    elif calc == "3":
       try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        if value2 != 0:
            print(value1 / value2)
        else:
            print("На ноль делить нельзя!")    
       except(ValueError):
        print("Вы ввели не число")
        continue

    elif calc == "10":
      try:
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1**value2)
      except(ValueError):
       print("Вы ввели не число")
       continue
    elif calc == " ":
       print("Введите одну из 9 операций")
    else:
       print("Введите одну из 9 операций")
     
    
loop = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить: ")
