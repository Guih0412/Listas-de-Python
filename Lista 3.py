# Lista 3 Python para Zumbis

# Exercicio 1: Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota= float(input("Digite sua nota entre 0 e 10: "))

while nota<0 or nota>10:
    nota= float(input("Digite novamente: "))

print(f"Sua nota é {nota}")



# Exercicio 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario= input("Digite seu usuario: ")
senha= input("Digite sua senha: ")

while usuario.lower() == senha.lower():
    print("\nSenha deve ser diferente de usuário")
    senha= input("Digite novamente sua senha: ")
   
print(f"\nUsuário: {usuario}")   
print(f"Senha: {senha}")



# Exercicio 3: Supondo  que  a  população  de  um  país  A  seja  da  ordem  de  80000  habitantes  com  uma  taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários  para  que  a  população  do  país  A  ultrapasse  ou  iguale  a  população  do  país  B, mantidas as taxas de crescimento.

cidade_a= 80000
cidade_b= 200000
ano= 0
while cidade_b>cidade_a:
    ano+=1
    cidade_a+= 0.03*cidade_a
    cidade_b+= 0.015*cidade_b
print(f"Cidade A irá ultrapassar cidade B em {ano} anos")



# Exercicio 4: A  seqüência  de  Fibonacci  é  a  seguinte:  1,  1,  2,  3,  5,  8,  13,  21,  34,  55,  ...  
# Sua  regra  de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
# Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

limite= int(input("Limite: "))
a,b=0,1

if limite==1:
    print(0)
else:
    while cont<=limite-2:
        a,b=b,b+a
        cont= cont+1
    print(b) 



# Exercicio 5: Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides. 

a= int(input("Digite um número: "))
b= int(input("Digite um número: "))

while b!=0:
    a,b=b,a%b
print(f"MDC é {a}")   
   
   