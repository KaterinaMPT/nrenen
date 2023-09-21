def is_even(number):
    result = number
    if result % 2 == 0:
        print ("true")
    else:
        print("false")
    return result
number = int(input("Введите число"))
print(is_even(number))