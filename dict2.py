

dicionario = {}


dicionario["Andre Nana"] = "Coordenador"


nome_colaborador = input("Informe o nome do colaborador: ")
cargo_colaborador = input("Informe o cargo do colaborador: ")

dicionario[nome_colaborador] = cargo_colaborador




for nome, cargo in dicionario.items():
    print("O colaborador {} atua no cargo de {}".format(nome,cargo))



dicionario["Andre Nana"] = "Stormtrooper"

for nome, cargo in dicionario.items():
    print("O colaborador {} atua no cargo de {}".format(nome,cargo))


print(dicionario.items())
