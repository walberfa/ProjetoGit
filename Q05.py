hs=0
mn=0
s=0
n=0
lista=[]
print("Sexo:\n 1-Masculino\n 2-Feminino\nVoc� gostou do produto?\n 1-Sim\n 2-N�o")
for i in range(10):
  lista.append(input("Digite separado por v�rgula:"))
  if(lista[i]=="1,1"): #Homens que votaram sim
    hs=hs+1
    s=s+1
  elif(lista[i]=="1,2"): #Homens que votaram n�o
    n=n+1
  elif(lista[i]=="2,1"): #Mulheres que votaram sim
    s=s+1
  elif(lista[i]=="2,2"): #Mulheres que votaram n�o
    mn=mn+1
    n=n+1
print("O n�mero de pessoas que respondeu sim foi: ",s)
print("O n�mero de pessoas que respondeu n�o foi: ",n)
print("O n�mero de homens que respondeu sim foi: ",hs)
print("O n�mero de mulheres que respondeu n�o foi: ",mn)