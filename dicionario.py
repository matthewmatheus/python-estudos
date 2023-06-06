



dicionario = {
    "Yoda":"Jedi Master",
    "Mace Windu":"Jedi Master",
    "Anakin SkyWalker":"Jedi Knight"}


for chave in dicionario.keys():
    print(chave)



print(dicionario["Yoda"])

print("----------------------------------------")

print(dicionario.items())

print("----------------------------------------")

for chave, valor in dicionario.items():

    print("{} -- {}".format(chave,valor))