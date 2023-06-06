soma_notas_impares = 0
soma_notas_pares = 0

print("Por favor, insira as notas dos alunos com números ímpares.")
i = 1
while i <= 49:
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(i) + ": "))
    soma_notas_impares += nota
    i += 2

print("Por favor, insira as notas dos alunos com números pares.")
i = 2
while i <= 50:
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(i) + ": "))
    soma_notas_pares += nota
    i += 2

media_impares = soma_notas_impares / 25
media_pares = soma_notas_pares / 25

print("A média das notas dos alunos ímpares é: " + str(media_impares))
print("A média das notas dos alunos pares é: " + str(media_pares))

if media_impares > media_pares:
    print("A metade dos alunos ímpares teve a maior nota.")
else:
    print("A metade dos alunos pares teve a maior nota.")
