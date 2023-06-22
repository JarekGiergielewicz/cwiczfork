# max()
# min()
# iter()
# reversed()
# next()
# slice()
# sorted()
# sum()
# input()

tab = [1, 0, 6, 99, -128, 33, 14, 4]

print(sorted(tab))
print(sum(tab))
print(max(tab))
print(min(tab))
print(list(reversed(tab)))

x = iter(tab)

print(next(x))
print(next(x))

print(slice(tab, 0, 2))

i = slice(2, 6)
print(tab[i])
print(tab[2:6])
print(sum(tab, (sum(tab))))






# i = 0
# m = 1
# while m < len(tab) - 1:
#     while m < len(tab) - 1:
#         if tab[i] > tab[m]:
#             x = tab[i]
#             tab[i] = tab[m]
#             tab [m] = x
#             i += 1
#     m += 1
#
# print(tab)
#
# tab = [1, 0, 6, 99, -128, 33, 14, 4]
# print(tab)

# def bubble_sort(tab):
#     length = len(tab)
#     for i in range(length-1):
#         j = 0
#         stop = length-1-i
#         while j < stop:
#             if tab[j] > tab[j+1]:
#                 tab[j], tab[j+1] = tab[j+1], tab[j]
#             j = j + 1
#     return tab

# print(bubble_sort(tab))

# n = len(tab)

# for i in range(n):
#
#     for j in range(0, n - 1):
#
#         if tab[j] > tab[j + 1]:
#             tab[j], tab[j + 1] = tab[j + 1], tab[j]
#
# print(tab)



# x = 0
# y = 0
# for i in tab:
#     if x <= i:
#         x = i
#     elif y >= i:
#         y = i
# print(x)
# print(y)

tab = [1, 0, 6, 99, -128, 33, 14, 4]
# print(tab)
#
# for i in range(len(tab)):
#
#     for j in range(len(tab) - i - 1):
#         print(tab)
#
#         if tab[j] < tab[j + 1]:
#             tab[j], tab[j + 1] = tab[j + 1], tab[j]
#
# print(tab)
#


