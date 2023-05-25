"""
  Operadores aritimetico:                Exemplos

  +  = adição                            5 + 2 == 7
  -  = subtração                         5 - 2 == 3
  *  = multiplicação                     5 * 2 == 10
  /  = divisão                           5 / 2 == 2.5
  ** = potência                          5 ** 2 == 25
  // = divisão inteira                   5 // 2 == 2
  %  = resto da divisão                  5 % 2 == 1


    Ordem de precedência:

    1 ()
    2 **
    3 *, /, //, %
    4 +, -



5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243


"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira {} e potencia {}'.format(di, e))




















