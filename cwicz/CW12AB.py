####### print("Zad. 1.")
# print("")
#
# def potega(a, b):
#     print("wynik potęgowania: ", a ** b)
#
# x = int(input("podaj pierwszą liczbę: "))
# y = int(input("podaj drugą liczbę: "))
#
# potega(x, y)
# #
#
# #####################

#
# print("")
# print("Zad. 2.")
# print("")



# def max_min (x):
#
#     a = 0
#     b = 0
#     for i in x:
#
#         if i <= a:
#             a = i
#         if i >= b:
#             b = i
#
#     print("minimum: ", a)
#     print("maximum: ", b)
#
# tab = [0, -2, 22, 10, 20, -3]
# max_min(tab)


#
# #####################
#

# print("")
# print("Zad. 3.")
# print("")



# def dodaj_(slowo):
#     py = slowo
#     L = len(py)
#
#
#     j = 0
#     w = ""
#     for i in py:
#          w += py[j]
#          j += 1
#          if j < L:
#            w += "_"
#     print(w)
# q = input("podaj słowo: ")
# dodaj_(q)



#
#
# #####################
#
#
# print("")
# print("Zad. 4.")
# print("")
#
# zdanie = "Ala ma kota"
# def odwrotnosc(a):
#     print(a)
#     print (a[: : -1])
#
#
# odwrotnosc("Ala ma kota")


#####################

# print("")
# print("Zad. 5.")
# print("")

def choinka(c, b):

    x = b
    y = " "
    L = c


    for i in range(L):
        print ((y * (L - i)), x * i, x, x * i)

ch = int(input("podaj wysokość choinki: "))
znak = input("podaj znak: ")
choinka(ch, znak)

######################
#
#
# print("")
# print("Zad. 6.")
# print("")


# def checkmon(x):
#     lista = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
#
#     a = x
#     j = 0
#
#     # for i in lista:
#     #     if i != a:
#     #          j += 1
#     #     else:
#     #         j += 1
#     #         print(j)
#     for i in lista:
#         if i != a:
#              j += 1
#         else:
#             j += 1
#             print(j)
#             break

# x = input("podaj nazwę miesiąca: ")
# checkmon(x)

# ######################
#
#
# print("")
# print("Zad. 7.")
# print("")


# def find_int_or_str(x):
#     tab = x
#     tab1 = "0123456789"
#     tab3 = "aAbBcCdDeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuWwXxYyZz"
#     a = 0
#     b = 0
#     for i in tab:
#
#         for j in tab1:
#             if i == j:
#                 a += 1
#                 break
#
#     for i in tab:
#
#         for m in tab3:
#             if i == m:
#                 b += 1
#                 break
#
#     print("cyfr jest: ", a)
#     print("liter jest: ", b)
# print("23rsett6L0")
# tab = "23rsett6L0"
# find_int_or_str(tab)


######################

# print("")
# print("Zad. 8.")
# print("")
#
#
#
# def check_Seasons(x, y):
#
#     m = y
#
#     d = x
#
#     if (m == 4) or (m == 3 and d >= 1) or (m == 5 and d <= 31):
#         return print("wiosna")
#
#     if  (m == 7) or (m == 6 and d >= 1) or (m == 8 and d <= 31):
#         return print("lato")
#
#     if  (m == 10) or (m == 9 and d >= 1) or (m == 11 and d <= 30):
#         return print("jesień")
#
#     if (m == 1) or (m == 12 and d >= 1) or (m == 2 and d <= 28):
#         return print("zima")
#
#
# x = int(input("podaj dzień: "))
# y = int(input("podaj miesiąc: "))
#
# check_Seasons(x, y)