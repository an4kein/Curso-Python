#!/usr/bin/env python3
#Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada

"""
number = int(input('Input: '))

dobro = number * 2
triplo = number * 3
raiz = number**(1/2)

print(f'Dobro: {dobro}, Triplo: {triplo}, Raiz: {raiz:.3f}')
"""

valor = int(input('Input: '))
print(' O Valor eh {},\n Dobro {}, \n Triplo {}, \n Raiz {}'.format(valor, (valor*2), (valor*3), (valor**(1/2))))