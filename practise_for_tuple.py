# Task 1
tuple001 = (42, "hello", 3.14, True, [1, 2, 3])
print(tuple001)

# Task 2
tuple002 = ("apple", "banana", "cherry", "date")
second_element = tuple002[1]
last_element = tuple002[-1]
print(second_element)
print(last_element)

# Task 3
tuple003 = (10, 20, 30, 40, 50, 60)
middle_3 = tuple003[2:5]
other = tuple003[::2]
print(middle_3)
print(other)

# Task 4
tuple004 = ("red", "green", "blue", "yellow")
green = "green" in tuple004
purple = "purple" not in tuple004
print(green)
print(purple)

# Task 5
tuple005 = (1, 2, 3, 4, 5, 6)
length = len(tuple005)
print(length)

# Task 6
tuple006 = ("a", "b", "c")
tuple007 = (1, 2, 3)
concatenated_tuple = tuple006 + tuple007
print(concatenated_tuple)

# Task 7
tuple008 = (1, 2, 2, 3, 4, 4, 4, 5)
count_of_4 = tuple008.count(4)
print(count_of_4)

# Task 8
tuple009 = ("cat", "dog", "bird", "fish")
dog = tuple009.index("dog")
print(dog)

# Task 9
tuple010 = ("Python", 3.10, "Programming")
language, version, topic = tuple010
print(language)
print(version)
print(topic)

# Task 10
tuple011 = (10, 20, 30)
#tuple011[0] = 15
#print(tuple011)