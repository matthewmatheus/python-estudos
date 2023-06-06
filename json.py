import json
from builtins import print


with open("C:\\Users\\Usuário\Documents\\dicionario.json","w", encoding="UTF-8") as arquivo:
    arquivo.write("Teste testando")

    print("Arquivo salvo")
    # print(arquivo.read)




#
# arquivo = open("C:\\Users\\Usuário\Documents\\dicionario.json","r", encoding="UTF-8")
# conteudo = arquivo.read()
# arquivo.close()
# agenda = json.loads(conteudo)
#
# print(type(agenda))


