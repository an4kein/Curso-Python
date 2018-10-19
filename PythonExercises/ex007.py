# Densenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota = float(input('Input nota: '))
nota2 = float(input('Input nota2: '))

total = nota + nota2

media = total / 2

print(f'Nota1: {nota}, Nota 2: {nota2}, Total: {total}, Media: {media}')

print('Nota1: {}, Nota2: {}, total: {}, Media {}.'.format(nota, nota2, (nota + nota2),))