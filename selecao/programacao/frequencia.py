import re

#Essa expressão regular checa se a entrada é um número inteiro qualquer, se não for, retorna None
def checa(mensagem):
    entrada = input(mensagem)
    regex = r'[0-9]*|[Ff]'
    if re.fullmatch(regex, entrada):
        return entrada
    else:
        return None
    
#Cria-se um dicionário para armazenar as frequências
frequencias = {}

#Loop infinito!
while True:
        #Lê o input do usuário e chama o método checa()
        entrada = checa("Digite um número inteiro ou 'f' para finalizar: ")
        
        match entrada:
            #Se a entrada é 'f', encerra o programa.
            case 'f'|'F':
                break
            #Se a entrada for None, o usuário digitou algo que não é um número. O loop reinicia.
            case None:
                continue
            #Qualquer outra entrada será um número inteiro.
            case _:
                #Se a entrada já estiver no dicionário, sua frequência é incrementada. Caso contrário, adiciona a chave com a frequência = 1
                if entrada in frequencias:
                    frequencias[entrada] += 1
                else:
                    frequencias[entrada] = 1

#Exibe as frequências de cada número
for numero, frequencia in frequencias.items():
    print(f"O número {numero} apareceu {frequencia} vezes")