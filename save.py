arquivo = open("C:\\Users\\Usuário\Documents\Visual Studio 2022\\test.txt", "w", encoding="UTF-8")

# print(arquivo.readlines())


for linha in arquivo.readlines():
    print(linha)

arquivo.close()


#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\Usuário\Documents\Visual Studio 2022\\teste.txt", encoding="UTF-8")

#Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))

#colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

#Exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)