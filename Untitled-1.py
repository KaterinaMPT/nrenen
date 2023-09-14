import math

loop = "y"

while loop == "y":
    print("Доступные операции:")
    print("1. Сложение двух чисел", "2. Вычитание чисел", "3. Деление чисел", "4. Умножение чисел", "5. Факториал числа")
    print("6. Квадратный корень числа", "7. Нахождение синуса", "8. Нахождение косинуса", "9. Нахождение тангенса", "10. Возведение в степень")
    oper = input("Введите операцию: ")
     
    if oper == "5":  
       
      factorial = int(input("Введите число: ")) 
      if factorial > 0: 
       for i in range(1, factorial): factorial = factorial * i 
       print(factorial) 
      elif factorial == 0:
       factorial = 1 
       print(factorial)
      else: 
       print("Не существует факториала отрицательного числа!")

    elif oper == "7":
        value = int(input("Введите число: "))
        print (("синус числа = "), math.sin(value))

    elif oper == "9":
      value = int(input("Введите число: "))
      print (("тангенс числа = "), math.tan(value))

    elif oper == "8":
      value = int(input("Введите число: "))
      print (("косинус числа = "), math.cos(value))

    elif oper == "6":
       value = int(input("Введите число: "))
       if value >= 1:
        print (("квадратный корень числа = "), math.sqrt(value))
       else:
        print("Такой корень посчитать нельзя")
       

    elif oper == "1":
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 + value2)

    elif oper == "2":
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 - value2)    

    elif oper == "4":
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1 * value2)   

    elif oper == "3":
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        if value2 != 0:
            print(value1 / value2)
        else:
            print("На ноль делить нельзя!")    

    elif oper == "10":
        value1 = float(input("Введите первое число: "))

        value2 = float(input("Введите второе число: "))
        print(value1**value2)
    elif oper == " ":
       print("Введите одну из 9 операций")
    else:
       print("Введите одну из 9 операций")
    
loop = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить: ")
