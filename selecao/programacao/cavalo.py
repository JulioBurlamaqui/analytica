import re

def checa():
    entrada = input()
    regex = r'[a-hA-H][1-8]'
    if(re.fullmatch(regex, entrada)):
        return (re.fullmatch(regex, entrada).group(0))
    else:
        return ''
    
origem = checa()
destino = checa()

if (origem != '') & (destino != ''):
    letra, numero = origem.split()
    unicode = ord(letra)
    casas = [[chr(unicode+1), str(numero+2)], [chr(unicode+1), str(numero-2)], [chr(unicode-1), str(numero+2)], [chr(unicode-1), str(numero-2)],
                [chr(unicode+2), str(numero+1)], [chr(unicode+2), str(numero-1)], [chr(unicode-2), str(numero+1)], [chr(unicode-2), str(numero-1)]]
    possivel = []
    for par in casas:
        possivel.append(''.join(par))
    if destino in possivel:
        print("VÁLIDO")
    else:
        print("INVÁLIDO")
else:
    print('Fim...')