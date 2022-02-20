#Gerador de senhas aleatórias.
import random

print("******* Gerador de Senhas [Mínimo 8 caracteres] *********")
quantidade_caracteres = int(input("Digite a quantidade de caracteres da sua senha: "))


#Lista de caracteres:
caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
    'a','b','c','d','f','e','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
            '$','&','_','-', '!','?']

#Função de gera a senha com caractereres aleatórios:
nsenha = ''
if quantidade_caracteres < 8:
    print("Digite valores maiores que 8")
else:
    for i in range(quantidade_caracteres):
        senha = random.choice(caracteres)
        nsenha += senha
    print(f'Sugestão de senha:  {nsenha} ')