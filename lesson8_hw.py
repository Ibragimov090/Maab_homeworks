#001
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

#002
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")

#003
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist!")

#004
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
except TypeError:
    print("Both inputs must be numerical!")

#005
try:
    with open("file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("You do not have permission to access this file!")

#006
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range!")

#007
try:
    num = int(input("Enter a number: "))
except KeyboardInterrupt:
    print("\nInput was interrupted!")

#008
try:
    result = 10 / 0
except ArithmeticError:
    print("An arithmetic error occurred!")

#009
try:
    with open("file.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Encoding issue occurred while reading the file!")

#010
my_list = [1, 2, 3]
try:
    my_list.append('a')
    my_list.insert(5, 'b')
except AttributeError:
    print("AttributeError occurred!")
