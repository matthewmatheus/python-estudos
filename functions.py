import calc
#importação de funções específica do módulo calc.py
from calc import subtrair

distancia = float(input("Insira a distancia percorrida: "))

tempo = float(input("Digite o tempo da viagem: "))

def calcularVelocidadeMedia(distancia, tempo):

    velocidade_media = distancia / tempo
    return print("A velocidade media é de {} km/h".format(velocidade_media))


calcularVelocidadeMedia(distancia, tempo)



valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = calc.somar(valor1, valor2)
subtracao = subtrair(valor2, valor1)
#exibindo a soma
print("A soma é {}".format(soma))

