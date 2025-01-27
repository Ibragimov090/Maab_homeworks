#001
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#002
n = int(input("Enter the number of lines to read: "))
with open("file.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end='')

#003
with open("file.txt", "a") as file:
    file.write("\nAppended text.")
with open("file.txt", "r") as file:
    print(file.read())

#004
n = int(input("Enter the number of lines to read from the end: "))
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end='')

#005
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines)

#006
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#007
import numpy as np
with open("file.txt", "r") as file:
    lines = np.array(file.readlines())
    print(lines)

#008
with open("file.txt", "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print(f"The longest word is: {longest_word}")

#009
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(f"The number of lines is: {len(lines)}")

#010
from collections import Counter
with open("file.txt", "r") as file:
    words = file.read().split()
    word_count = Counter(words)
    print(word_count)

#011
import os
file_size = os.path.getsize("file.txt")
print(f"The file size is: {file_size} bytes")

#012
my_list = ["Hello", "World", "Python"]
with open("file.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

#013
with open("file1.txt", "r") as file1, open("file2.txt", "w") as file2:
    content = file1.read()
    file2.write(content)

#014
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    for line1, line2 in zip(lines1, lines2):
        print(line1.strip() + " " + line2.strip())

#015
import random
lines = open("file.txt", "r").readlines()
print(random.choice(lines))

#016
with open("file.txt", "r") as file:
    print(file.closed)

#017
with open("file.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)

#018
with open("file.txt", "r") as file:
    content = file.read()
    words = content.replace(',', ' ').split()
    print(f"The number of words is: {len(words)}")

#019
with open("file.txt", "r") as file:
    content = file.read()
    characters = list(content)
    print(characters)

#020
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(letter)

#021
with open("file.txt", "w") as file:
    for i in range(0, 26, 5):
        file.write(''.join(string.ascii_uppercase[i:i+5]) + '\n')
