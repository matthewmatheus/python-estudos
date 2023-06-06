minutos_atuais = int(input("Insira quantos minutos marcam agora no relógio: "))
fatorial = 1

for i in range(1, minutos_atuais + 1):
    fatorial *= i
print("A senha para liberação da maquina é LIBERDADE{}".format(fatorial))
