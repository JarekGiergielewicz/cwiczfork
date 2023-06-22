# class AreaRect:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b
#
#     def calculate_area(self):
#         return self.l * self.b
#
# area1 = AreaRect(20, 4)
# area2 = AreaRect(21, 4)
# area2.l = 7
# AreaRect.
# print(area1.calculate_area())
#
# print(area2.calculate_area())


# class Employer:
#
#     def __init__(self, fname, lname, email):
#         self.fname = fname
#         self.lname = lname
#         self. email = email
#
#     def Geetings(self):
#         print("hej " + self.fname)
#
#     def Fname(self):
#         print("Masz fajne nazwisko: " + self.lname)
#
#     def Mail(self):
#         print("Twoj mil to: " + self.email)
#
# empl1 = Employer("Jarek", "Gier", "j@g.pl")
#
# print(empl1.Geetings())
# print(empl1.Fname())
# print(empl1.Mail())
# empl2 = Employer("ja", "ty", "o@o.pl")
#
# print(empl2.Mail())
#
# print(5)
# print(6)

# class Employee:
#
#     def __init__(self, fname, lname, email):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#
#     def greet_person(self):
#         print("hello, your name is: " + self.fname)
#
# peroson01 = Employee("Jarek","Giergielewicz", "j@j.pl")
# peroson02 = Employee("Krzysiek","Giergielewicz", "K@j.pl")
#
# print(peroson01.lname)
# print(peroson01.fname)
# print(peroson01.email)
# print(peroson02.email)

# print(peroson01.greet_person())

# class Obliczanie_oszczędnosci:
#     odsetki = 0.01
#     def __init__(self, name, stan, odsetki):
#         self.name = name
#         self.stan = stan
#         # self.odsetki = odsetki
#
#     def Oszczednosci(self):
#         return " {x} Twoje odsetki to: ".format(x = self.name), self.stan * self.odsetki
#         # return f"{self.name} twoje odsetki to {self.odsetki}"
#         # return "{x} twoje odsetki to {y}".format(x = self.name, y = self.stan)
# klient_01 = Obliczanie_oszczędnosci("Jarek", 10000, 0.06)
# klient_02 = Obliczanie_oszczędnosci("Marta", 23560, 0.04)
# klient_01.odsetki = 0.03
# print(klient_01.Oszczednosci())
# print(klient_02.Oszczednosci())
#
#
# def test_test ():
#     klient03 = Obliczanie_oszczędnosci("Jarek", 10000, 0.06)
#     return klient03.Oszczednosci()
#
#
#
# print(test_test())


# class Pierwsza:
#
#     def __init__(self):
#
#         print ("pierwsza klasa")
#
#     def Druk01(self):
#
#         print("Pierwsza 1")
#
#
#
# class Druga(Pierwsza):
#
#     def __init__(self):
#         print ("druga klasa")




# d = Druga()
# p = Pierwsza()
# d.Druk01()

# def Test_PD():
#     P = Druga()
#     P.Druk01()
#
# Test_PD()


class Działania_Mat:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Dodawanie(self):
       return self.x + self.y


    def Odejmowanie(self):
        return self.x - self.y






class D_M(Działania_Mat):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Mnozenie(self):
        return self.x * self.y

    def Dzielenie(self):
        return self.x / self.y


class Petla(D_M):
    def __init__(self, zmienna, dlug):
        self.zmienna = zmienna
        self.dlug = dlug

    def Pentlaa(self):
        for i in range(self.dlug):
            print(i + self.zmienna)


# tab_01 = [1, 2, 3, 4, 5, 6]
#
#
# tab_01.reverse()
#
# print(tab_01)
#
#
# for i in range(len(tab_01)):
#
#     for j in range(len(tab_01) - 1):
#         if tab_01[j] > tab_01[j + 1]:
#             tab_01[j], tab_01[j + 1] = tab_01[j + 1], tab_01[j]
#
#
# print(tab_01)


class Tab_operation:

    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1-i):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr

# s = Tab_operation(tab_01)
# print(s.bubble_sort())

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# arr = [2, 3, 1, 4, 5]


# arr.pop(0)
# arr.append(88)
# arr.remove(88)
# print(arr.count(3))
# print(sum(arr))
# print(slice(arr))
# w = "t a"
# z = w.split()
# print(z)
# print(arr)













#
# d = Działania_Mat(1, 0)
# m = D_M(3, 2)
#
# print(m.Mnozenie())
#
# print(m.Dodawanie())
#
# print(d.Odejmowanie())
#
# print(m.Dzielenie())






# class AreaRect:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b
#
#     def calculate_area(self):
#         return self.l * self.b
#
# area1 = AreaRect(20, 4)
# area2 = AreaRect(21, 4)
# area2.l = 7
#
# print(area1.calculate_area())
#
# print(area2.calculate_area())










