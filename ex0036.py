valorcasa = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual seu salário?R$ '))
anos = int(input('Quantos anos deseja pagar '))
prestacao= valorcasa /(anos*12)
minimo= salario * 30/100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valorcasa, anos), end='')
print(' a prstação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo ACEITO')
else:
    print('Emprestimo NEGADO')












