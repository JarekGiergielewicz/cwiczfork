from shop_function import *



def shoping():

    gender = input("Podaj płeć M/K: ").upper()

    age = int(input("Podaj wiek: "))
    if age < 18:
        return print("jesteś za młody na zakupy")
    else:

        financial = int(input("Podaj finanse: "))
        rate = float(input("Podaj kurs USD: "))

        finan = currency_exchange(financial, rate)
        ability = financial_ability(gender, age, finan)
        print(shop_ability(ability))



shoping()

# x = True
#
# while x == True:
#     gender = input("Podaj płeć M/K: ").upper()
#     if gender == "K":
#         x = False
#     else:
#         x = True

