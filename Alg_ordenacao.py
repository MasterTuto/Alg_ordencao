""" Algoritmos de ordenação

Esse programa apresenta um comparativo do tempo de execução dos métodos BubbleSort, InsertionSort, QuickSort e sort (método do python)

Nos testes, são ordenados números interios de 0 até 1000000

O programa é executado com 500, 1.000 e 5.000 números. Com cada uma das três quantidades de números, deve-se testar o vetor com números aleatórios, ordenados em ordem crescente e ordenados em ordem decrescente.



"""
import random
import time
import sys

sys.setrecursionlimit(1000000)



#BubbleSort
def bubbleSort(alistf):
    for passnum in range(len(alistf)-1,0,-1): #Percorre toda a lista do ultimo para o primeiro
        for i in range(passnum): #Percore o total de vezes e diminui um para cada rodada
            if alistf[i]>alistf[i+1]: #Se o numero atual for menor que o proximo altera a ordem dos dois
                temp = alistf[i]
                alistf[i] = alistf[i+1]
                alistf[i+1] = temp



#InsertionSort
def insertionSort(alistf):
   for index in range(1,len(alistf)): #percorre a lista do primeiro para o ultimo
     currentvalue = alistf[index] #armazena o valor no vetor do elemento atual na variavel currentvalue
     position = index #armazena o valor do indice na variavel position
     while position>0 and alistf[position-1]>currentvalue: #faz um loop para encontrar a posição correta do valor armazenado em currentvalue
         alistf[position]=alistf[position-1]
         position = position-1

     alistf[position]=currentvalue #aramzena o valor de currentvalue na posição correta



#QuickSort
def quickSort(alistf):
   quickSortHelper(alistf,0,len(alistf)-1)


def quickSortHelper(alistf,first,last):
   if first<last:

       splitpoint = partition(alistf,first,last)

       quickSortHelper(alistf,first,splitpoint-1)
       quickSortHelper(alistf,splitpoint+1,last)


def partition(alistf,first,last):
    pivotvalue = alistf[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alistf[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alistf[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alistf[leftmark]
            alistf[leftmark] = alistf[rightmark]
            alistf[rightmark] = temp

    temp = alistf[first]
    alistf[first] = alistf[rightmark]
    alistf[rightmark] = temp

    return rightmark


#Chamada dos metodos
alist = random.sample(range(1000000), 500) #cria uma lista com os valores do teste, usar 500, 1.000 e 5.000
#alist.sort() #utilize para testar com a lista ordenada em ordem crescente
#alist.sort(reverse=True) #utilize para testar com a lista em ordem decrescente

alisttemp = alist[:]
print(alisttemp[0:5])
inicio = time.time()
bubbleSort(alisttemp)
fim = time.time()
print("Tempo do BubbleSort (s) - " + str(fim - inicio))
print(alisttemp[0:5])

alisttemp = alist[:]
print(alisttemp[0:5])
inicio = time.time()
insertionSort(alisttemp)
fim = time.time()
print("Tempo do InsertionSort (s) - " + str(fim - inicio))
print(alisttemp[0:5])

alisttemp = alist[:]
print(alisttemp[0:5])
inicio = time.time()
quickSort(alisttemp)
fim = time.time()
print("Tempo do QuickSort (s) - " + str(fim - inicio))
print(alisttemp[0:5])

alisttemp = alist[:]
print(alisttemp[0:5])
inicio = time.time()
alisttemp.sort()
fim = time.time()
print("Tempo do método Sort (s) - " + str(fim - inicio))
print(alisttemp[0:5])