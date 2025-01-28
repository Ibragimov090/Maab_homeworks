#001
stringbek = 'hello'
stringbek1 = 'assalom'
stringbek2 = 'abcabcdabcdeabcdefabcdefg'

countbek = 0
setbek = set()
result = ''
prev = ''

for i in stringbek2:
    countbek += 1
    if countbek >= 3:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            if i not in setbek:
                setbek.add(i)
                result += i
                result += '_'
                countbek = 0
            else:
                result += i
        else:
            result += i
    else:
        result += i


if result[-1] == '_':
    print(result[:-1])
else:
    print(result)
#002
list1 = [1, 2, 3, 3, 4]
list2 = [1, 6, 7]
uncommon = []
for num in list1:
    if num not in list2:
        uncommon.append(num)
for num in list2:
    if num not in list1:
        uncommon.append(num)
print(uncommon)  


