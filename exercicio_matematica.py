#Dizer se um número é par ou ímpar

def num_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input(' Digite um número: '))

if num_par(numero):
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

