"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangete desse angulo

"""
import math
angulo = float(input('Digite o angulo que vc deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENo de {:.2f} '.format(angulo, seno))

