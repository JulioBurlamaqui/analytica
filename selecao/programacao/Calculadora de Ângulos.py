import re

def checa():
    horario = input()
    regex = r'([0-1][0-9]|[2][0-3]):[0-5][0-9]|[Ff]'
    if(re.fullmatch(regex, horario)):
        return (re.fullmatch(regex, horario).group(0))
    else:
        return None

horario = checa()
print(horario)

match horario:
    case 'f'|'F':
        print('Fim...')
    case None:
        print('Input inválido') 
    case _:
        hora, minuto = int(horario.split(':'))
        if(hora > 11):
            hora -= 12
        angulo = (hora*60 - 11*minuto)/2
        print('O menor ângulo é de %d°', angulo)

