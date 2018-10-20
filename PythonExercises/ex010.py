# Crie um programa que leia o quanto em dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere US$=1,00 = RS$3.27


carteira = float(input('insert: '))
dolar = carteira / 3.27
print(dolar)
print('Com R$ {:.2f} voce pode comprar US$ {:.2f}'.format(carteira, (carteira/3.27)))

