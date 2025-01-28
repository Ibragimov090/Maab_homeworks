#001
dict001 = {'a': 3, 'b': 1, 'c': 2}
sorted_asc001 = dict(sorted(dict001.items(), key=lambda x: x[1]))
sorted_desc001 = dict(sorted(dict001.items(), key=lambda x: x[1], reverse=True))
print(sorted_asc001, sorted_desc001)

#002
dict002 = {0: 10, 1: 20}
dict002[2] = 30
print(dict002)

#003
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dict003 = {**dic1, **dic2, **dic3}
print(dict003)

#004
dict004 = {'a': 1, 'b': 2}
key004 = 'a'
exists004 = key004 in dict004
print(exists004)

#005
dict005 = {'a': 1, 'b': 2, 'c': 3}
for k005, v005 in dict005.items():
    print(k005, v005)

#006
n006 = 5
dict006 = {x: x * x for x in range(1, n006 + 1)}
print(dict006)

#007
dict007 = {x: x * x for x in range(1, 16)}
print(dict007)

#008
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict008 = {**dict1, **dict2}
print(dict008)

#009
dict009 = {'x': 10, 'y': 20}
for k009, v009 in dict009.items():
    print(k009, v009)

#010
dict010 = {'x': 5, 'y': 15}
sum010 = sum(dict010.values())
print(sum010)

#011
dict011 = {'x': 2, 'y': 3}
product011 = 1
for v011 in dict011.values():
    product011 *= v011
print(product011)

#012
dict012 = {'x': 10, 'y': 20}
dict012.pop('x', None)
print(dict012)

#013
keys013 = ['a', 'b', 'c']
values013 = [1, 2, 3]
dict013 = dict(zip(keys013, values013))
print(dict013)

#014
dict014 = {'c': 3, 'a': 1, 'b': 2}
sorted_dict014 = dict(sorted(dict014.items()))
print(sorted_dict014)

#015
dict015 = {'a': 5, 'b': 3, 'c': 8}
max015 = max(dict015.values())
min015 = min(dict015.values())
print(max015, min015)

#016
class Obj016:
    def __init__(self):
        self.x = 1
        self.y = 2
obj016 = Obj016()
dict016 = vars(obj016)
print(dict016)

#017
dict017 = {'a': 1, 'b': 2, 'c': 1}
unique017 = {k: v for k, v in dict017.items() if list(dict017.values()).count(v) == 1}
print(unique017)

#018
dict018 = {}
is_empty018 = not bool(dict018)
print(is_empty018)

#019
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
dict019 = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
print(dict019)

#020
data020 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique020 = set(v for d in data020 for v in d.values())
print(unique020)
