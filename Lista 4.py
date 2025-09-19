# Lista 4 Python para Zumbis

# Exercicio 1: Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random
numeros= random.sample(range(1,101),10)

menor=numeros[0]
maior=numeros[0]

for numero in numeros:
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
        
print(f"Vetor: {numeros}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print("")



# Exercicio 2: Sorteie  20  inteiros  entre  1  e  100  numa  lista.  Armazene  os  números  pares na  lista  PAR  e  os números ímpares na lista IMPAR. Imprima as três listas.

import random
numeros= random.sample(range(1,101),20)

par=[]
impar=[]

for numero in numeros:
    if numero%2==0:
        par.append(numero)
    else:
        impar.append(numero)
print(f"Vetor: {numeros}")
print(f"Pares: {par}")
print(f"Impares: {impar}")
print("")


# Exercicio 3: Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
# Gere um terceiro vetor  de  20  elementos, cujos valores  deverão  ser  compostos  pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

import random

v1= random.sample(range(1,101),20)
v2= random.sample(range(1,101),20)
v3= []

for i in range(20):
    v3.append(v1[i])
    v3.append(v2[i])
print(f"Vetor 1: {v1}")
print(f"Vetor 2: {v2}")
print(f"Vetor 3: {v3}")  
print("")
    
    
# Exercicio 4: Seja o  statement sobre diversidade:
# “The Python Software Foundation and the global Python community  welcome  and  encourage  participation  by  everyone.  Our  community  is  based  on mutual respect, tolerance, and encouragement, and we are working to help each other live up to  these  principles.  We  want  our  community  to  be  more  diverse:  whoever  you  are,  and whatever  your  background,  we  welcome  you.”.
# Gere  uma  lista  de  palavras  deste  texto  com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”.
# Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.

texto= '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''

texto= texto.lower()
texto= texto.replace(",",'') 
texto= texto.replace(".",'')
texto= texto.replace(":",'')
texto= texto.split()

lista=[]
for palavra in texto:
    if palavra[0] in 'python' or palavra[-1] in 'python':
        lista.append(palavra)
print("Palavras que começam ou terminam com uma das letras de Python")        
print(lista)    
print("")    
    
    
    
# Exercicio 5: Seja  o  mesmo  texto  acima  “splitado”. Calcule  quantas  palavras  possuem  uma  das  letras “python” e que tenham mais de 4 caracteres.
# Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.

texto= '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''

texto= texto.lower()
texto= texto.replace(",",'') 
texto= texto.replace(".",'')
texto= texto.replace(":",'')
texto= texto.split()

lista=[]
for palavra in texto:
    for letra in palavra:
      if letra in 'python' and len(palavra)>4:
        lista.append(palavra)
        break
print(f"Há {len(lista)} palavras com mais de 4 letras e que contém uma das letras de Python ")
print(lista)      