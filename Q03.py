lista = []
while True:
  num = int(input("Digite um n�mero: "))
  if num==0:
    break
  lista.append(num)
soma = 0
for i in lista:
  soma = soma + i
media=soma/len(lista)
print("\nA m�dia �:",media)
cont=0
for i in lista:
  if i > media:
    cont=cont+1
if cont==1:
  print("\nExiste",cont,"n�mero acima da m�dia.")
else:
    print("\nExistem",cont,"n�meros acima da m�dia.")