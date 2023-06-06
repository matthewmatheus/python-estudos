#primeiro importamos o módulo sys
import sys
#depois criamos algumas variáveis de exemplo
nome = "Bruce Wayne"
idade = 30
peso = 92.3
#Vamos exibir em uma mensagem o nome da variável, o tipo (type) e o tamanho (getsizeof)
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

#primeiro importamos o módulo sys
import sys
#agora vamos criar uma lista vazia
lista = []
#E verificar o tamanho
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista), sys.getsizeof(lista)))


#criação da tupla
tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)

#exibição da tupla
print(f"A tupla foi criada assim: {tupla}")

#contagem de elementos
contagem = tupla.count(7)
print(f"Nessa tupla o número {7} aparece {contagem} vezes")

#índice em que encontrou o valor
indice = tupla.index(11)
print(f"O número {11} foi encontrado no índice: {indice}")