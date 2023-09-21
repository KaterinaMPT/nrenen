def sum_digits(number):
   if number < 10:
     return number
   else:
        return number % 10 + sum_digits(number // 10)
number = int(input("Введите число"))
print(sum_digits(number))
    
    