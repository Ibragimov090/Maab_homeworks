# Task 1
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.extend(["grape", "kiwi"])
print(fruits)

# Task 2
numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)

# Task 3
colors = ["red", "green", "blue", "yellow", "blue"]
colors.remove("blue")
print(colors)

# Task 4
animals = ["cat", "dog", "bird", "fish"]
index_of_bird = animals.index("bird")
print(index_of_bird)

# Task 5
numbers_count = [1, 2, 3, 4, 1, 2, 1]
count_1 = numbers_count.count(1)
print(count_1)

# Task 6
integers = [5, 10, 15, 20, 25]
integers.reverse()
print(integers)

# Task 7
numbers_sort = [7, 3, 9, 1, 5]
numbers_sort.sort()
print(numbers_sort)
numbers_sort.sort(reverse=True)
print(numbers_sort)

# Task 8
cities = ["New York", "Paris", "Tokyo", "Sydney"]
cities_copy = cities.copy()
print(cities_copy)
cities.append("London")
print(cities)
print(cities_copy)

# Task 9
random_numbers = [8, 4, 6, 2, 9]
random_numbers.clear()
print(random_numbers)

# Task 10
months = ["January", "February", "March", "April", "May"]
last_month = months.pop()
print(last_month)
second_month = months.pop(1)
print(second_month)
print(months)