# Lista 2 Python para Zumbis

# Exercicio 1: Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

L1= int(input("Lado 1: "))
L2= int(input("Lado 2: "))
L3= int(input("Lado 3: "))

if L1<=0 or L2<=0 or L3<=0:
    print("Nao pode ser 0 ou negativo")
elif L1<=L2+L3 or L2<=L1+L3 or L3<=L1+L2:
    print("Um lado nao pode ser maior que soma dos dois")  
else:
    if L1==L2==L3:
        print("É triangulo equilátero")
    elif L1!=L2 and L1!=L3 and L2!=L3:
        print("É triangulo escaleno")
    else:
        print("É triangulo isósceles")



# Exercicio 2: Determine se um ano é bissexto.

year= int(input("Digite ano: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("É bissexto")
else:
    print("Não é bissexto")    



# Exercicio 3: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado  de  São  Paulo  (50  quilos)  deve  pagar  uma  multa  de  R$  4,00  por  quilo  excedente.
# João  precisa  que  você faça  um  programa  que  leia  a  variável  peso  (peso  de  peixes)  e  verifique  se  há  excesso.
# Se  houver,  gravar  na variável  excesso  e  na  variável  multa  o  valor  da  multa  que  João  deverá  pagar.
# Caso  contrário  mostrar  tais variáveis com o conteúdo ZERO.

peso= float(input("Digite o peso do peixe: "))

if peso<=50:
    print("Sem Multa")
else:
    excesso= peso-50
    multa= 4*excesso
    print(f"Excesso de {excesso:.2f} quilos. Multa de R${multa:.2f}")
    
    
    
# Exercicio 4: Faça um Programa que leia três números e mostre o maior deles.

n1= float(input("Digite N1: "))    
n2= float(input("Digite N2: "))
n3= float(input("Digite N3: "))

if n1>n2 and n1>n3:
    print("n1 é maior")
elif n2>n1 and n2>n3:
    print("n2 é maior")
elif n3>n2 and n3>n1:
    print("n3 é maior")
else:
    print("Nenhum numero é maior")



# Exercicio 5: Faça um Programa que leia três números e mostre o maior e o menor deles.

n1= float(input("Digite N1: "))    
n2= float(input("Digite N2: "))
n3= float(input("Digite N3: "))

if n1>n2>n3:
    print("n1 é maior e n3 é menor")
elif n1>n3>n2:
    print("n1 é maior e n2 é menor")
elif n2>n1>n3:
    print("n2 é maior e n3 é menor")
elif n2>n3>n1:
    print("n2 é maior e n1 é menor")    
elif n3>n2>n1:
    print("n3 é maior e n1 é menor")
elif n3>n1>n2:
    print("n3 é maior e n2 é menor")
    
    

# Exercicio 6: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%  para  o  INSS  e  5%  para  o  sindicato,  faça  um  programa  que  nos  dê  o  salário  bruto,  quanto  pagou  ao  INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

salario_hora= float(input("Salário por hora: "))
horas_mes= float(input("Horas trabalhadas por mes: "))

salario_bruto= salario_hora * horas_mes
imposto_renda= 0.11 * salario_bruto
inss= 0.08 * salario_bruto
sindicato= 0.05 * salario_bruto
salario_liquido= salario_bruto - imposto_renda - inss - sindicato

print(f"Desconto do imposto de renda: {imposto_renda:.2f}")
print(f"Desconto do inss: {inss:.2f}")
print(f"Desconto do sindicato: {sindicato:.2f}")
print(f"Salario liquido: {salario_liquido:.2f}")



# Exercicio 7: Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em  latas  de  18  litros,  que  custam  R$  80,00.
# Informe  ao  usuário  a  quantidades  de  latas  de  tinta  a  serem compradas e o preço total. 
# Obs. : somente são vendidos um número inteiro de latas.

metros= float(input("Digite medida em metros a ser pintada: "))
if metros%54==0:
    latas= metros/54
else:
    latas= int(metros/54)+1
    
valor= latas*80
print(f"Numero de latas: {latas}")
print(f"Preço: {valor:.2f}")
