demo_dict = {"kulcz01":"ogórki", "klucz02":"ogrodnika", "klucz03": "corki"}
print(type(demo_dict))
print(demo_dict)

#

demo_dict["klicz4"] = "ogorki"
print(demo_dict)
demo_dict.update({"klucz06":"ogorki"})
print(demo_dict)

print(demo_dict["klicz4"])
print(demo_dict)


# get / [] podaje wartoś pod kluczem
print(demo_dict.get("klucz03"))

# keys - podaje listę kluczy
print(demo_dict.keys())

# values - podaje listę wartosci
print(demo_dict.values())

# items - podaje listę klucz + jego wartosc
print(demo_dict.items())

# pop - usuwa dany klucz, popitem usuwa ostatni ze słownika
print(demo_dict)
demo_dict.pop("klicz4")
print(demo_dict)

demo_dict.popitem()
print(demo_dict)

# update - dodaje klucz i wartosc
# zmienna["klucz"] = "wartosc"
demo_dict.update({"klucz20":"ogórki01"})
demo_dict["klucz21"] = "pomidory"
print(demo_dict)

# copy - tworzy kopie słownika

demo_dict01 = demo_dict.copy()

print(demo_dict01)

demo_dict01.update({"klucz00":"sałata"})
print(demo_dict01)

demo_dict01.pop("kulcz01")
print(demo_dict01)

print(demo_dict01.get("klucz20"))

print(demo_dict.keys())
print(demo_dict.values())
print(demo_dict01.items())

for i in demo_dict01:
    print(demo_dict01.get(i))
