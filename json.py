import json
from builtins import print


arquivo = open("C:\\Users\\Usuário\Documents\\dicionario.json","r", encoding="UTF-8")
conteudo = arquivo.read()
arquivo.close()
agenda = json.loads(conteudo)

print(type(agenda))
