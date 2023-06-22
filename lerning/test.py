from class_object import Tab_operation

tab_03 = [2, 3, 4]

dd = Tab_operation(tab_03)

print(dd.bubble_sort())



x = "ala ma kota"

x.count("a")
print(x.find("k"))

tab_03.remove(3)
print(tab_03)

tab04 = [5, 6, 10, -1, -99, 10000, 2793, 292992, 888]

f = Tab_operation(tab04)
print(f.bubble_sort())

g = Tab_operation([3, 0, 1, 4])
print(g.bubble_sort())

y = [3, 0, 1, 4]

# print(y.index(0))
# print(y[0])
#
# print(len(y))

for g in range(len(y)):
    print(y[g])


a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Vicky"]

x = set(zip(a, b))
print(x)






x.add("mike")
print(x)