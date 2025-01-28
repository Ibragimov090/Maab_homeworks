#001
set001 = set()
print(set001)

#002
set002 = {1, 2, 3, 4}
for elem002 in set002:
    print(elem002)

#003
set003 = {1, 2, 3}
set003.add(4)
set003.update([5, 6])
print(set003)

#004
set004 = {1, 2, 3, 4}
set004.remove(3)
set004.discard(2)
print(set004)

#005
set005 = {1, 2, 3}
item005 = 3
if item005 in set005:
    set005.remove(item005)
print(set005)

#006
set006_1 = {1, 2, 3}
set006_2 = {2, 3, 4}
intersection006 = set006_1 & set006_2
print(intersection006)

#007
set007_1 = {1, 2, 3}
set007_2 = {3, 4, 5}
union007 = set007_1 | set007_2
print(union007)

#008
set008_1 = {1, 2, 3}
set008_2 = {3, 4, 5}
difference008 = set008_1 - set008_2
print(difference008)

#009
set009_1 = {1, 2, 3}
set009_2 = {3, 4, 5}
symmetric_difference009 = set009_1 ^ set009_2
print(symmetric_difference009)

#010
set010_1 = {1, 2, 3}
set010_2 = {1, 2}
is_subset010 = set010_2 <= set010_1
print(is_subset010)

#011
set011 = {1, 2, 3}
copy011 = set011.copy()
print(copy011)

#012
set012 = {1, 2, 3}
set012.clear()
print(set012)

#013
frozenset013 = frozenset([1, 2, 3])
print(frozenset013)

#014
set014 = {10, 20, 5, 15}
max014 = max(set014)
min014 = min(set014)
print(max014, min014)

#015
set015 = {1, 2, 3, 4}
length015 = len(set015)
print(length015)

#016
set016 = {1, 2, 3}
value016 = 2
is_present016 = value016 in set016
print(is_present016)

#017
set017_1 = {1, 2, 3}
set017_2 = {4, 5, 6}
no_common017 = set017_1.isdisjoint(set017_2)
print(no_common017)

#018
set018_1 = {1, 2, 3}
set018_2 = {1, 2}
is_superset018_1 = set018_1 >= set018_1
is_superset018_2 = set018_1 >= set018_2
print(is_superset018_1, is_superset018_2)

#019
set019_1 = {1, 2, 3}
set019_2 = {2, 3, 4}
difference019 = set019_1 - set019_2
print(difference019)

#020
set020_1 = {1, 2, 3, 4}
set020_2 = {3, 4, 5}
set020_1 -= set020_2
print(set020_1)
