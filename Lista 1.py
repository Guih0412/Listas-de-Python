# Lista 1 Python para Zumbis

# Exercicio 1: Faça um programa que peça dois números inteiros e imprima a soma desses dois números.

n1= int(input("Digite o número: "))
n2= int(input("Digite o numero: "))



soma= n1+n2
print(f"A soma é {soma}")





# Exercicio 2: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metro= float(input("Digite a medida: "))

milimetro= metro * 1000
print(f"A medida é {milimetro:.2f}")



# Exercicio 3:  Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dia= int(input("Digite o numero de dias: "))
hora= int(input("Digite o numero de horas: "))
minuto= int(input("Digite o numero de minutos: "))
segundo= int(input("Digite o numero de segundos: "))

total= 86400*dia + 3600*hora + 60*minuto + segundo

print(f"O tempo total é de {total} segundos")



# Exercicio 4: Faça  um  programa  que  calcule  o  aumento  de  um  salário.
# Ele  deve  solicitar  o  valor  do  salário  e  a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario= float(input("Digite seu salario: "))
porcentagem_aumento= float(input("Digite porcentagem de aumento: "))

aumento= salario*porcentagem_aumento/100
salario_total= salario + aumento

print(f"O aumento foi de {aumento:.2f}")
print(f"Salario atual é de {salario_total:.2f}")



# Exercicio 5: Solicite  o  preço  de  uma  mercadoria  e  o  percentual  de  desconto.
# Exiba  o  valor  do  desconto  e  o preço a pagar.

preco= float(input("Digite o preço: "))
porcentagem_desconto= float(input("Digite porcentagem de desconto: "))

desconto= preco*porcentagem_desconto/100
preco_total= preco - desconto

print(f"O desconto foi de {desconto:.2f}")
print(f"preco atual é de {preco_total:.2f}")



# Exercicio 6:  Calcule  o  tempo  de  uma  viagem  de  carro.
# Pergunte  a  distância  a  percorrer  e  a  velocidade  média esperada para a viagem.

distancia= float(input("Digite a distancia: "))
velocidade= float(input("Digite a velocidade: "))
tempo= distancia/velocidade
print(f"Tempo é de {tempo}")



# Exercicio 7: Converta uma temperatura digitada em Celsius para Fahrenheit.
# F = 9*C/5 + 32

celsius= float(input("Digite a temperatura: "))
fahrenheit= celsius*9/5+32
print(f"Temperatura em fahrenheit é de {fahrenheit}")



# Exercicio 8: Faça agora o contrário, de Fahrenheit para Celsius.

fahrenheit= float(input("Digite a temperatura: "))
celsius= (fahrenheit-32)*5/9
print(f"Temperatura em celsius é de {celsius}")



# Exercicio 9: Escreva  um  programa  que  pergunte  a  quantidade  de  km  percorridos  por  um  carro  alugado  pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

distancia= float(input("Digite a distancia em km: "))
dias= float(input("Digite o número de dias: "))
preco= (60*dias)+(0.15*distancia)
print(f"O preço é {preco}")



# Exercicio 10: Escreva  um  programa  para  calcular  a  redução  do  tempo  de  vida  de  um  fumante.
# Pergunte  a quantidade  de  cigarros  fumados  por  dia  e  quantos  anos  ele  já  fumou.
# Considere  que  um  fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
# Exiba o  total de dias.

cigarros_dia= int(input("Digite número de cigarros por dia: "))
anos_fumando= int(input("Digite número de anos fumando: "))

tempo_perdido_minutos= 10*cigarros_dia*365*anos_fumando
tempo_perdido_dias= tempo_perdido_minutos/1440

print(tempo_perdido_dias)



# Exercicio 11: Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

digitos= len(str(2**1000000))
print(f"O numero de digitos de 2 elevado a um milhao é de {digitos}")
