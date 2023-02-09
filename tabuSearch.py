import numpy as np
import random
#import math

count = 0;

# Lendo o arquivo e usando sua primeira linha para saber o tamanho da matriz

filename = "./Entradas/"+input("Nome do arquivo: ")

arq = open(filename, 'r')
#arq = open('./Entradas/Entrada 10.txt', 'r')

primeiraLinha = arq.readline()
arq.close()
numeroMatriz = int(primeiraLinha)
auxM = np.zeros((numeroMatriz+1, numeroMatriz))

#=============================================

#arq = open('./Entradas/Entrada 10.txt', 'r')
arq = open(filename, 'r')

# Transformando os dados do arquivo em uma matriz

for linha in arq:
  auxLinha = linha
  Lista = auxLinha.split()
  nums = [int(s) for s in Lista]
  auxM[count,:] = nums[:]
  count = count+1

auxM = np.delete(auxM, (0), 0)

listaPercorrida = []
maiorDistancia = numeroMatriz + 1

while (len(listaPercorrida) < numeroMatriz):
    ca = random.randrange(0, numeroMatriz)
    listaPercorrida = []
    listaPercorrida.append(ca)
    
    menDis = 0
    
    while menDis < maiorDistancia:
        proxCidade = 0
        menDis = maiorDistancia
        for cd in range(numeroMatriz):
            for j in range(len(listaPercorrida)):
                if not(cd in listaPercorrida):
                    if auxM[ca][cd] != 0:
                        if auxM[ca][cd] < menDis:
                            menDis = auxM[ca][cd]
                            proxCidade = cd
                        
        if menDis != maiorDistancia:
            listaPercorrida.append(proxCidade)
            ca = proxCidade
    print(len(listaPercorrida))