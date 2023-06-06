bpm = int(input("informe seus BPMs: "))
idade = int(input("iforme sua idade: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Os batimentos estao dentro da media")
    else:
        print("Batimentos fora da media")

elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Os batimentos estao dentro da media")
    else:
        print("Batimentos fora da media")

elif idade >= 18 and idade <= 59:
    if bpm >= 70 and bpm <= 80:
        print("Ta bao")
    else:
        print("ta ruim, vai ver isso ai")

elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Ta bao")
    else:
        print("ta ruim, vai ver isso ai veio")


time1 = int(input("goals time 1"))
time2 = int(input("goals time 2"))

if time1 > time2 :
    print("vitoria time 1")

elif time2 > time1:
    print("vitoria time 2")

elif time1 == time2:
    print("empate")
    