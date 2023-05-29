largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
quantidade_tinta = area / 2

print("A área da parede é:", area, "metros quadrados.")
print("Será necessária uma quantidade de", quantidade_tinta, "litros de tinta para pintá-la.")
