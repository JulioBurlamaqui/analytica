import re

#Essa expressão regular checa se a entrada é uma casa existente, se não for, retorna string vazia
def checa(mensagem):
    entrada = input(mensagem)
    regex = r'[a-hA-H][1-8]|[Ff]'
    if re.fullmatch(regex, entrada):
        return entrada
    else:
        return ''
    
print("Diremos se uma movimentação do cavalo no xadrez é legal\n")

#Loop infinito!
while True:
    #Lê os inputs do usuário e chama o método checa()
    origem = checa("Digite a casa de origem\n")
    destino = checa("Digite a casa de destino\n")
    
    #Primeiro, colocamos a string em letra minúscula, então testamos se é igual a 'f', pois assim, é válido para 'F' e 'f'.
    #Caso um dos imputs seja, o programa termina
    if origem.lower() == 'f' or destino.lower() == 'f':
        print('Fim...')
        break
    #Caso um dos inputs seja igual a palavra vazia, significa que o usuário digitou pelo menos um input inválido. O loop é reiniciado.
    elif origem == '' or destino == '':
        print('Input inválido\n')
        continue

    #É criado uma lista que vai conter os caracteres (letra e número) da casa de origem   
    caracteres = []
    #É inserido nesta lista cada caractere da casa de origem
    for caractere in origem:
        caracteres.append(caractere)
    #Separamos letra e número
    letra = caracteres[0]
    numero = int(caracteres[1])
    #Transformamos a letra no seu valor unicode
    unicode = ord(letra)
    #A lista casa possui 8 listas de tamanho 2 dentro de si. Cada uma com um dos movimentos do cavalo a partir da casa de origem 
    # mesmo que ele caia fora do tabuleiro
    casas = [[chr(unicode+1), str(numero+2)], [chr(unicode+1), str(numero-2)], [chr(unicode-1), str(numero+2)], [chr(unicode-1), str(numero-2)],
                [chr(unicode+2), str(numero+1)], [chr(unicode+2), str(numero-1)], [chr(unicode-2), str(numero+1)], [chr(unicode-2), str(numero-1)]]
    #A lista possível vai unir essas 8 listas menores, chamadas de par
    possivel = []
    for par in casas:
        possivel.append(''.join(par))
    #Caso o destino esteja entre essas 8 listas, a movimento é legal. Caso não esteja, ilegal. O destino já foi checado se é casa válida.
    if destino in possivel:
        print("VÁLIDO\n")
    else:
        print("INVÁLIDO\n")