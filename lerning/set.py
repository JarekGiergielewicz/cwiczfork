
set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 8, 5, 9}
print(set_1)
print(len(set_1))


print(set_2)
print(len(set_2))

# add - dodaje element do zbioru
set_1.add(10)
print(set_1)
# remove / discard - usuwa element ze zbioru
set_1.remove(1)
set_1.discard(2)
print(set_1)

# pop - usuwa losowy element ze zbioru

set_2.pop()
print(set_2)

# union połączenie zbiorów z robieniem nowej zmiennej
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 5, 6, 7, 8, 5, 9}
print(set_1 , set_2)
set_3 = set_1.union(set_2)
print(set_3)

# update - bez robienia nowej zmiennej

set_1.update(set_2)
print(set_1)

# intersection - cześć wspólna 2 zbiorów z robieniem nowej zmiennej

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 5, 6, 7, 8, 5, 9}

set_3 = set_1.intersection(set_2)
print(set_3)

# intersection_update - cześć wspólna 2 zbiorów BEZ robieniem nowej zmiennej

set_1.intersection_update(set_2)
print(set_3)

# symmetric_difference - pozostawia to co różne w 2 zbiorach z robieniem zmiennej
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 5, 6, 7, 8, 5, 9}

set_3 = set_1.symmetric_difference(set_2)
print(set_3)

# symmetric_difference_update - pozostawia to co różne w 2 zbiorach BEZ robieniem nowej zmiennej
set_1.symmetric_difference_update(set_2)
print(set_1)

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 5, 9}
print(set_1)
print(set_2)

# issubset czy pierwszy zbiór zawiera sie w drugim
z = set_1.issubset(set_2)
print(z)
z = set_2.issubset(set_1)
print(z)

# issuperset czy drugi zbiór zawiera sie w pierwszym
z = set_1.issuperset(set_2)
print(z)

z = set_2.issuperset(set_1)
print(z)

