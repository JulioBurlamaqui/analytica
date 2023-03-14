import re
import math

#Essa expressão regular checa se o horário está no formato desejado, se não for, retorna None
def checa(mensagem):
    horario = input(mensagem)
    regex = r'([0-1][0-9]|[2][0-3]):[0-5][0-9]|[Ff]'
    if re.fullmatch(regex, horario):
        return horario
    else:
        return None

#Loop infinito!
while True:
    #Lê o input do usuário e chama o método checa()
    horario = checa("Digite as horas de um relógio no formato hh:mm e diremos o menor ângulo entre seus ponteiros.\nDigite 'F' para o programa terminar\n")

    match horario:
        #Se a entrada for "F", o programa encerra
        case 'f'|'F':
            print('Fim...')
            break
        #Se a entrada for None quer dizer que o usuário não digitouo horário está no formato desejado
        case None:
            print('Input inválido\n') 
        #Como qualquer outra entrada fora aprovada pela expressão regular, podemos usar o case default
        case _:
            #Divide-se hora e minuto com base no caractere ':'
            hora = int(horario.split(':')[0])
            minuto = int(horario.split(':')[1])
            #Como foi indicado no comando da questão que a hora está no formado 24h, devemos subtrair 12h caso o horário seja 
            # superior a 12 para que o ângulo fique dentro do relógio de ponteiros.
            if(hora > 12):
                hora -= 12
            #Fórmula para o ângulo dos ponteiros de um relógio
            angulo = math.fabs((hora*60 - 11*minuto)/2)
            #Se o ângulo for maior que 180, estaremos pegando o ângulo maior, então subtraimos ele de 360 para obtermos o ângulo menor
            if angulo > 180:
                angulo = 360 - angulo
            #Exibimos a respostas para o usuário
            print(f'O menor ângulo é de {angulo}°\n')

