# x = 0
#
# while x <= 10:
#     print(x)
#     x += 1
#     if x == 5:
#         print(x)
#         break

cities = ["Sydney","Delhi", "Mumbai", "Mumbai", "melborne", "Kolkata","Amehdabad"]

for i in cities:
    print(i)

slowo = "Jarek Giergielewicz"

for i in slowo:
    print(i)

slownik = {"kulcz01":"ogórki", "klucz02":"ogrodnika", "klucz03": "corki"}

for i in slownik:
    print(slownik.get(i))


tab = [("jarek", "Gier"), ("ela", "wojciech"), ("agata", "mastalska"), ("agnieszka", "kurpinska")]
print(tab)

for i in  tab:
    print(i)

tab_name = [ ]
tab_secname = [ ]
tab_name01 = [4, 2, 3, 1]
for name, secname in tab:
    tab_name.append(name)
    tab_secname.append(secname)
print(tab_name)
print(tab_secname)

tab_2 = zip(tab_name, tab_secname, tab_name01)
tab_3 = list(tab_2)
print(tab_3)
print(len(tab_3))

for i, l, m in tab_3:
    print(m, i, l)

demo_direct = {"key01": tab, "key02": tab}
print(demo_direct)

for i, j in demo_direct.items():

    for m in j:
        
        for c in m:
            print(c)






