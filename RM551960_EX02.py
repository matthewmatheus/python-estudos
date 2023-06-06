print("Insira a quantidade de votos referente a cada dia da semana")
votos_segunda = int(input("Votos para SEGUNDA-FEIRA: "))
votos_terca = int(input("Votos para TERÇA-FEIRA: "))
votos_quarta = int(input("Votos para QUARTA-FEIRA: "))
votos_quinta = int(input("Votos para QUINTA-FEIRA: "))
votos_sexta = int(input("Votos para SEXTA-FEIRA: "))

maior_voto = 0
dia_mais_votado = ""

if votos_segunda > maior_voto:
    maior_voto = votos_segunda
    dia_mais_votado = "SEGUNDA-FEIRA"

if votos_terca > maior_voto:
    maior_voto = votos_terca
    dia_mais_votado = "TERÇA-FEIRA"

if votos_quarta > maior_voto:
    maior_voto = votos_quarta
    dia_mais_votado = "QUARTA-FEIRA"

if votos_quinta > maior_voto:
    maior_voto = votos_quinta
    dia_mais_votado = "QUINTA-FEIRA"

if votos_sexta > maior_voto:
    maior_voto = votos_sexta
    dia_mais_votado = "SEXTA-FEIRA"

print("O dia mais votado foi: ", dia_mais_votado)

