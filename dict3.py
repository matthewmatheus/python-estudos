import json


contatos = {
    "Clark Kent":{
    "celular":"123456",
    "email":"clark@kypto.com"
    },
    "Steph Curry":{
    "celular":"333333",
    "email":"stepth@curry.com"
    }
}

# print(json.dumps(contatos, indent=4))

arquivo = open("C:\\Users\\Usuário\Documents\\dicionario.json", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)
arquivo.close()


# for nome,formas_contato in contatos.items():
#
#     print("O contato {}".format(nome))
#
#     for forma,valor in formas_contato.items():
#      print("Pode ser contatado pelo seu {} atraves do {}".format(forma,valor))
#
# print("\n\n")
