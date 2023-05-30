"""
exemplos de como se utilizar "bibliotecas" do pyton

import = bebidas = café, agua, refrigerante
from bebida import = café

biblioteca padrão = math

math - ela te da possibilidades de usar

ceil =  arredonda o numero pra cima
floor = arredondamento para baixo
trunc = eliminitar numero depois da virgula
pow = potencia
sqrt = calcular raiz quadrada
factorial = calculo fatorial

exemplo: import math (importa todas essas funcionalidades da blibioteca "math"
         from match import sqrt ( importa apenas a sqrt)

"""

from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {} '.format(num, ceil(raiz)))



import random

numero = random.randint(1,10)
print(numero)

import emoji

print(emoji.emojize(":smile:", language='alias'))


