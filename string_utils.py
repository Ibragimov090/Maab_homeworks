def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in vowels:
            count += 1
    return count

