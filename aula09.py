"""
Manipulando cadeias de texto

string = cadeia de texto/caracteres

* Fatiamento

Exemplo:

C u r s o     e m   V   i   d   e  o   P  y  t  h  o   n
1 2 3 4 5  6  7 8   9  10  11  12  13...              20

    frase[9] = V

    frase[9:13] = V i d e       13 = o ( ele não coloca o "o" que seria o 13

    frase[9:21] = v i d e o  p y t h o n

    frase[9:21:2] = V d o P t o   (saltando de dois em dois)

    frase[:5] = C u r s o

    frase[15:] =   P y t h o n      (começa pelo caractere 15 e vai até o final)

    frase [9::3] = V e P h (pulando de 3 em 3 até o final)


        * Análise

    len(frase) = curso em video python = 21 caracteres

    frase.count('o') = contar quantas vezes aparece o caractere na frase ( o )
    3 'o' na frase = curso em video python

    frase.count('o', 0, 13)
     1 'o' na frase, pois ele n conta o 13

    frase.find('deo') = quantas vezes ele encontrou certa frase
     começou na posição 11 da frase



"""

frase = 'curso em video python'
frase2 = '   Aprenda Python  '

print(frase.find('Android'))
print('curso' in frase)
print(frase.replace('python', 'Android'))

print(frase.upper())
print(frase.lower())

print(frase.capitalize())
print(frase.title())

print(frase2)
print(frase2.strip())

print(frase2.rstrip())
""" remove apenas o lado direito de caracteres vazios"""

print(frase.lstrip())
""" remove apenas o lado esquerdo de caracteres vazios"""

"""
Divisão

"""

print(frase.split())
print('-'.join(frase))























