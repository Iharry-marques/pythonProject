
salario = float(input('Qual é o salário do funcionário ? R$'))
aumento = salario + (salario * 15/100)

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))

"""
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 1.15

print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}')

"""