#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

    # criação de uma lista com os nomes dos Jedi
    jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
    # Removendo um valor específico da lista
    jedi.remove("Yoda")
    # A variável assumirá cada um dos valores da lista
    for nome in jedi:
        # para cada volta do loop, exibir o valor assumido
        print(nome)

        # criação de uma lista com os nomes dos Jedi
        jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
        # Removendo um valor em uma posição específica
        jedi.pop(2)
        # A variável assumirá cada um dos valores da lista
        for nome in jedi:
            # para cada volta do loop, exibir o valor assumido
            print(nome)
