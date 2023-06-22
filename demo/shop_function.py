def currency_exchange(pln, kurs):
    return round(pln / kurs)

def financial_ability(gender, age, finan):
    if age < 18:
        return 0
    else:

        if gender == "M" and age >= 60 or gender == "K" and age >= 70:
            if finan >= 2000:
                return  finan
            else:
                return 0
        else:
            if finan >= 300:
                return finan
            else:
                return 0

def shop_ability(ability):
    if ability == 0 or ability <= 270:
        return "Nie możesz nic zakupić, brak zdolości kredytowej"
    else:
        if ability > 300:
            return "Możesz kupić pralkę"
            # print("Możesz kupić pralkę")
        if ability > 600:
            # print("Możesz kupić telewizor")
            return "Możesz kupić telewizor"
        # if ability > 1000:
        #     return "stać cie na wszystko"














