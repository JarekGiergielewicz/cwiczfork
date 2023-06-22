from shop_function import *

# print(currency_exchange(100))

def test_currency_exchange():
    assert currency_exchange(100) == 23

def test_financial_ability():
    assert financial_ability("M", 10, 5000) == 0

def test_shop_ability():
    assert shop_ability(270) == "Możesz kupić pralkę"

# print(shop_ability(401))