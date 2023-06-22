cities = ["Sydney","Delhi", "Mumbai", "Mumbai", "melborne", "Kolkata","Amehdabad"]

print(cities)

# INDEX podaje index dla zapytania
print(cities.index("Delhi"))

# COUNT liczy ilość elementow zapytania

print(cities.count("Mumbai"))

# SORT sortuje alfabetycznie
cities.sort()
print(cities)

# REVERSE odwraca kolejnosc elementow
cities.reverse()
print(cities)

# COPY
cities_new_list = cities.copy()
print(cities_new_list)

# APPENDED dodaje element na koniec list

cities.append("Polska")
print(cities)

# INSERT dodaje na pozycje indeksu element
cities.insert(2, "Polska")
print(cities)

# REMOVE usuwa pierwszy z listy podany element
cities.remove("Polska")
print(cities)

# POP usuwa element na podanym indeksie
cities.pop(7)
print(cities)

# CLEAR czysci listę

cities.clear()
print(cities)

cities = ["Sydney","Delhi", "Mumbai", "Mumbai", "melborne", "Kolkata","Amehdabad"]

print(cities)

cities.insert(1, "Polska")
print(cities)
cities.pop(1)
print(cities)




