import re

#Essa expressão regular checa se a entrada está no valor esperado, se não for, retorna None
def checa(mensagem):
    entrada = input(mensagem)
    regex = r'[0-9]+.[0-9][0-9]'
    if re.fullmatch(regex, entrada):
        return float(entrada)
    else:
        return None

#Declaração de todas as variáveis
cem, cinquenta, vinte, dez, cinco, dois, um, pcinquenta, pvinteECinco, pdez, pcinco, cent = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

#Lê o input do usuário e chama o método checa()
pagamento = checa("Insira um valor monetário com duas casas decimais para que ele seja decomposto em notas e moedas.\n")

#Se o retorno de checa for None, o usuário não digitou um valor válido e o programa acaba
if pagamento is None:
    print("Valor inválido\nFim...")
    
else:
    #Se o montante for maior que o valor de uma cédula, pegamos a parte inteira da divisão e alocamos na respectiva variável e passamos 
    #resto para a cédula seguinte.
    if pagamento >= 100:
        cem = int(pagamento//100)
        pagamento %= 100
    if pagamento >= 50:
        cinquenta = int(pagamento//50)
        pagamento %= 50
    if pagamento >= 20:
        vinte = int(pagamento//20)
        pagamento %= 20
    if pagamento >= 10:
        dez = int(pagamento//10)
        pagamento %= 10
    if pagamento >= 5:
        cinco = int(pagamento//5)
        pagamento %= 5
    if pagamento >= 2:
        dois = int(pagamento//2)
        pagamento %= 2
    if pagamento >= 1:
        um = int(pagamento//1)
        pagamento -= 1
    #Aqui, multiplicamos o montante por 100 para resolver de maneira análoga a de cima
    pagamento *= 100
    if pagamento >= 50:
        pcinquenta = int(pagamento//50)
        pagamento %= 50
    if pagamento >= 25:
        pvinteECinco = int(pagamento//25)
        pagamento %= 25
    if pagamento >= 10:
        pdez = int(pagamento//10)
        pagamento %= 10
    if pagamento >= 5:
        pcinco = int(pagamento//5)
        pagamento %= 5
    if pagamento >= 1:
        cent = int(pagamento//1)

    print("NOTAS\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\n\nMOEDAS\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01"
          .format(cem, cinquenta, vinte, dez, cinco, dois, um, pcinquenta, pvinteECinco, pdez, pcinco, cent))
