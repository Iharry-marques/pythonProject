"""
dias_a = int(input('Digite a quantidade de dias percorridos: '))
km_p = float(input('Digite a quantidade de km percorrido: '))

preco_dia = 60
preco_km = 0.15

preco_total = (km_p * preco_km) + (dias_a * preco_dia)

print('O valor total a ser pago é: R$ {:.2f} '.format(preco_total))

"""

dias = int(input('Quantos dias alugado? :'))
km = float(input('Quantos Km rodados? :'))
pago = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é: R$ {:.2f} '.format(pago))
