g = open("2023-02-26.txt", "r")
# print(g.read())
# g.close()

print(g.readline())
g.close()


g = open("2023-02-26.txt", "r")
# print(g.read())
# g.close()

print(g.readline())

x = g.read().upper().split()

print(x)
g.close()

with open("plik_txt_WITH", "a") as fw:
    fw.write(" coś tam, coś tam " + "\n")

with open("plik_txt_WITH", "r") as fr:
    print(fr.read())

