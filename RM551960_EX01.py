tipoAssinatura = input("Insira o tipo de sua assinatura: ")
faturamentoAnual = float(input("Qual o valor do seu faturamento anual? "))
porcentagem = 0
invalido = True

while invalido:

    if tipoAssinatura == "Basic":
        porcentagem = faturamentoAnual * 0.3
        print("O valor que deve ser pagar ao estúdio é de {}".format(porcentagem))
        invalido = False

    elif tipoAssinatura == "Silver":
        porcentagem = faturamentoAnual * 0.2
        print("O valor que deve ser pagar ao estúdio é de {}".format(porcentagem))
        invalido = False

    elif tipoAssinatura == "Gold":
        porcentagem = faturamentoAnual * 0.1
        print("O valor que deve ser pagar ao estúdio é de {}".format(porcentagem))
        invalido = False

    elif tipoAssinatura == "Platinum":
        porcentagem = faturamentoAnual * 0.05
        print("O valor que deve ser pagar ao estúdio é de {}".format(porcentagem))
        invalido = False

    else:
        tipoAssinatura = input("Tipo de assinatura inválido. Por favor insira aqui novamente seu tipo de assinatura: ")
