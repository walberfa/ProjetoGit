print("Digite os angulos de um triangulo:")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
t = a+b+c
if t!=180:
  print("Voc� digitou �ngulos inv�lidos.")
else:
  if a==90 or b==90 or c==90:
    print("O tri�ngulo � ret�ngulo.")
  elif a>90 or b>90 or c>90:
    print("O tri�ngulo � obtus�ngulo")
  else:
    print("O tri�ngulo � acut�ngulo")