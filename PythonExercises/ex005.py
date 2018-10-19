#faca um programa que leia um numero e mostre na tela seu sucessor e seu antecessor.

"""
valor = int(input('input: '))
anti = valor - 1
suce = valor + 1

print(f'O valor inserido foi, {valor} e seu antecessor eh {anti} e o sucessor eh {suce}')
"""

valor = int(input('Input: '))
print('O valor eh {}, seu antecessor eh {}, e seu sucessor eh {}'.format(valor, (valor-1),(valor+1)))
