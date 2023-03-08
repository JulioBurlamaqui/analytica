pagamento = float(input())
cem, cinquenta, vinte, dez, cinco, dois, um, pcinquenta, pvinteECinco, pdez, pcinco, cent = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

if(pagamento >= 100):
    cem = pagamento//100
    pagamento %= 100
if(pagamento >= 50):
    cinquenta = pagamento//50
    pagamento %= 50
if(pagamento >= 20):
    vinte = pagamento//20
    pagamento %= 20
if(pagamento >= 10):
    dez = pagamento//10
    pagamento %= 10
if(pagamento >= 5):
    cinco = pagamento//5
    pagamento = pagamento % 5
if(pagamento >= 2):
    dois = pagamento//2
    pagamento %= 2
if(pagamento >= 1):
    um = pagamento//1
    pagamento = (pagamento - 1) * 100
if(pagamento >= 50):
    pcinquenta = pagamento//50
    pagamento %= 50
if(pagamento >= 25):
    pvinteECinco = pagamento//25
    pagamento = pagamento % 25
if(pagamento >= 10):
    pdez = pagamento//10
    pagamento %= 10
if(pagamento >= 5):
    pcinco = pagamento//5
    pagamento = pagamento % 5
if(pagamento >= 1):
    cent = pagamento//1

print("NOTAS\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\n\nMOEDAS\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01"
      .format(cem, cinquenta, vinte, dez, cinco, dois, um, pcinquenta, pvinteECinco, pdez, pcinco, cent))
