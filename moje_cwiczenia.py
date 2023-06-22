# znajdowanie najniższej for
lista = [0, -1, 3, 1]
# a = 0
# b = 0
# for i in lista:
#     a = i
#     i = b
#     b = i
#
#
#     if a <= b:
#         b = a
#
# print(b)

# znajdowanie najniższej while

# a = 0
# b = 1
#
# L = len(lista)
# while b < L - 1:
#     if lista[a] >= lista[b]:
#         a = b
#     b = b + 1

# print(lista[a])

# bombelkowe for
# i = 0
# b = 0
# x = 0
# n = 0
# for j in lista:
#
#     for i in lista:
#         # x, i = i, b
#         # b = x
#         # if i > b:
#         #     lista[]
#         x = i
#         i = b
#         b = x
#         if i > b:
#             a = lista[n]
#             lista[n] = lista[n + 1]
#             lista[n + 1] = a
#
# print(lista)




#bombelkowe while
# j = 0
# while j < len(lista) -1:
#      i = 0
#      while i < len(lista) -1 :
#
#           if lista[i] > lista[i + 1]:
#               a = lista[i]
#               lista[i] = lista[i + 1]
#               lista[i + 1] = a
#
#           i = i + 1
#      j = j + 1
#      print(lista)

# porzadkowanie przez redukcje

a = 0
b = 1

L = len(lista)
while b < L:
    if lista[a] > lista[b]:
        a = b
    b = b + 1

x = lista[a]
a = a + 1


print(lista[a])
L = len(tab)
    n = 0   #indeks po którym chodzimy
    while n < L-1:
        i = find_min_index(tab, n, L)
        if i != n:
            swap(tab, i, n)
        n += 1
    print(tab)

    tab = [8, 2, 1, 1, 5, 5]
    [1, 1, 2, 2, 5, 5]