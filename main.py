metros = float(input("degite os metros quadrados a ser pintado:"))
litros = metros/3
lata = litros/18
preco = lata*80
if lata > 1:
  print(f"latas que sera usadas:{lata:.1f}")
  print(f"preço total das latas:${preco:.2f}")
else:
  print(f"sera usado {lata:.1f}% de uma lata")
  print(f"preço da lata é:$80")