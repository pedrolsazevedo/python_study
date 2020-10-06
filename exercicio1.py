
#!/usr/bin/env python3
totalEcoTP = 0
totalEcoTG = 0

# Informações sobre a lata de tinta de 24L
lataGrandePreco = 91
lataGrandeTamanho = 24

# Informações sobre a lata de tinta de 5.4L
lataPequenaPreco = 23
lataPequenaTamanho = 5.4

# Área de cobertura por L
areaCobertaTinta = 7

# Calculo do total de area coberta pela tinta de 24L
lataGrandeArea = (lataGrandeTamanho * areaCobertaTinta)

# Calculo do total de area coberta pela tinta de 5.4L
lataPequenaArea = round((lataPequenaTamanho * areaCobertaTinta), 2)

#  Informa o total de área coberta pela tinta de 24L
## print('Área total coberta pela lata de 24L:',lataGrandeArea)
#  Informa o total de área coberta pela tinta de 5.4L
## print("Área total coberta pela lata de 24L:",lataPequenaArea)

print("Entre com a área necessária para pintar:")
clienteAreaparaPintar = input()
clienteAreaparaPintar = float(clienteAreaparaPintar)

# Total de tintas grandes
def usoTintasGrandes(clienteAreaparaPintar):
  
  # Checa se o total inserido é menor ou igual a area do cliente, se for o total de latas é = 1
  if (clienteAreaparaPintar <= lataGrandeArea):
    totalTG = 1
  # Se o total a area para pintar for maior que a area coberta pela tinta executa o processo
  elif (clienteAreaparaPintar > lataGrandeArea):
    # Divide o total da area para pintar pelo total de area coberta pela tinta
    totalTG = clienteAreaparaPintar / lataGrandeArea
    # Se tiver alguma sobra X.01 por exemplo, adiciona uma lata de tinta.
    if (totalTG % 1 != 0):
      totalTG = int(totalTG) + 1

  return totalTG

# Total de tintas pequenas
def usoTintasPequenas(clienteAreaparaPintar):
  
  # Checa se o total inserido é menor ou igual a area do cliente, se for o total de latas é = 1
  if (clienteAreaparaPintar <= lataPequenaArea):
    totalTP = 1
  # Se o total a area para pintar for maior que a area coberta pela tinta executa o processo
  elif (clienteAreaparaPintar > lataPequenaArea):
    # Divide o total da area para pintar pelo total de area coberta pela tinta
    totalTP = clienteAreaparaPintar / lataPequenaArea
    # Se tiver alguma sobra X.01 por exemplo, adiciona uma lata de tinta.
    if (totalTP % 1 != 0):
      totalTP = int(totalTP) + 1

  return totalTP


## def melhorUsoTintas(clienteAreaparaPintar):
areaPinturaEconomica = clienteAreaparaPintar

while areaPinturaEconomica > 0: 
  
  if areaPinturaEconomica >= lataGrandeArea:
     totalEcoTG = totalEcoTG + 1
     areaPinturaEconomica = areaPinturaEconomica - lataGrandeArea

  if (areaPinturaEconomica <= lataPequenaArea):
     totalEcoTP = totalEcoTG + 1
     areaPinturaEconomica = areaPinturaEconomica - lataPequenaArea

  if ((areaPinturaEconomica > lataPequenaArea) and (areaPinturaEconomica < lataGrandeArea)):
     totalEcoTG = totalEcoTG + 1
     areaPinturaEconomica = areaPinturaEconomica - lataGrandeArea



# Envia o valor da area para pintar para a funcao
totalTGFinal = usoTintasGrandes(clienteAreaparaPintar)
totalTPFinal = usoTintasPequenas(clienteAreaparaPintar)

# Faz o calculo de custo
precoTintaGrande = totalTGFinal * lataGrandePreco
precoTintaPequena = totalTPFinal * lataPequenaPreco
precoEconomico = (totalEcoTG * lataGrandePreco)+(totalEcoTG * lataPequenaPreco)

print('a) ',totalTGFinal,' lata(s) de 24 litros: R$', precoTintaGrande)
print('b) ',totalTPFinal,' lata(s) de 5.4 litros: R$', precoTintaPequena)
print('c) ',totalEcoTG,' lata(s) de 24 litros e ',totalEcoTG, 'lata(s) de 5.4 litros: R$: ',precoEconomico)