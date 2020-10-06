import math

print("Entre valor do lado do Hexagono:")
ladoHex = input()
ladoHex = float(ladoHex)

diamentro = ladoHex * 2
area = (((ladoHex**2)*(math.sqrt(3))/4)*6)
perimetro = ladoHex * 6

print('Lado do hexagono: ',ladoHex,' metros,')
print('Area: ',area,' metros quadrados,')
print('Perimetro: ',perimetro,' metros.')