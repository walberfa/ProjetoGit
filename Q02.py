qtd = int(input("Dgite a quantidade de ma��s: "))
if qtd < 12:
  valor = qtd*0.3
else:
  valor = qtd*0.25
print(qtd, " ma��s custam R$",valor)