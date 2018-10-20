#Faca um programa que leia um numero inteiro e mostre na tela a sua tabuada.

multi = int(input('Input: '))
'''
for c in range(1,11):
    print(multi * c)
    
'''
print('-' * 15)
print('{} x {:2} = {}'.format(multi, 1, (multi*1)))
print('{} x {:2} = {}'.format(multi, 2, (multi*2)))
print('{} x {:2} = {}'.format(multi, 3, (multi*3)))
print('{} x {:2} = {}'.format(multi, 4, (multi*4)))
print('{} x {:2} = {}'.format(multi, 5, (multi*5)))
print('{} x {:2} = {}'.format(multi, 6, (multi*6)))
print('{} x {:2} = {}'.format(multi, 7, (multi*7)))
print('{} x {:2} = {}'.format(multi, 8, (multi*8)))
print('{} x {:2} = {}'.format(multi, 9, (multi*9)))
print('{} x {:2} = {}'.format(multi, 10, (multi*10)))
print('-' * 15)