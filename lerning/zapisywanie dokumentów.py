import datetime

f = open("proba.txt", "w")
f.write("Próbny tekst")
f.close()

tab = ["Ala", 1, 5, "ma", "kota"]

n = open("lista.txt", "w")
n.write(str(tab))
n.close()

x = open("lisa02.txt", "w")

for i in tab:
    x.write(str(i) + "\n")
x.close()

# current_data_time = str(datetime.datetime.today().date())
def Test_demo (x):
     current_data_time = str(datetime.datetime.today().date())
     file = open("{}.txt".format(current_data_time), "a")
     file.write(x + "\n")



Test_demo("ala ma kota")




