qtd = int(input("Digite a quantidade de numeros a serem cadastrados:"))
contatos = []
numeros = []
for i in range(qtd):
  contatos.append(input("\nNome:"))
  numeros.append(input("Telefone:"))
while True:
  consulta = input("\nQual nome que voc� deseja consultar o telefone?")
  if consulta in contatos:
    a = contatos.index(consulta)
    print("N�mero:",numeros[a])
  else:
    print("Nome n�o cadastrado")
  x = int(input("\nDeseja pesquisar outro n�mero?\n1-Sim\n2-N�o\n"))
  if x == 2:
    break