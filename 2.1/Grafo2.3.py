import networkx as nx
import matplotlib
import pylab as plt
from networkx import minimum_spanning_tree
from networkx.algorithms import node_classification

Grafo = nx.Graph()
Arbol= nx.Graph()
archivo = open("Bianca.txt", "r")
numerodenodos = int(archivo.readline())

for n in range(0,numerodenodos):
    archivo.readline()

numerodearistas = int(archivo.readline())

for n in range(0,numerodearistas):
    arista1 = archivo.readline()
    separador= " "
    arista = arista1.split(separador)
    nodo1=arista[0]
    nodo2=arista[1]
    Grafo.add_edge(nodo1, nodo2, weight=1)


T = nx.minimum_spanning_tree(Grafo)
sorted(T.edges(data=True))

print(Grafo.edges)

R = nx.difference(Grafo, T)
R = list(R.edges)

Arbol = Grafo

for n in range(0,len(R)):
    nodo1 = R[n][0]
    nodo2 = R[n][1]
    Arbol.remove_edge(nodo1, nodo2)



Listanodos= list(Grafo.nodes)
listedges= list(Arbol.edges)

CPC=[]

for n in range(0, len(Listanodos)):
    if len(Arbol.edges(Listanodos[n]))==1:
        nodo = Listanodos[n]
        print(nodo)
        for m in range(0, len(listedges)):
            if listedges[m][0] == nodo or listedges[m][1] == nodo:
                nodo1 = listedges[m][0]
                nodo2 = listedges[m][1]
                if nodo1 == nodo:
                    nodo11 = nodo1
                    nodo22 = nodo2
                if nodo2 == nodo:
                    nodo11 = nodo2
                    nodo22 = nodo1

                CPC.append([nodo1, nodo2])
                Arbol.remove_edge(nodo1, nodo2)
                Listanodos.remove(nodo)
                Arbol.remove_node(nodo11)
                print(CPC)
                if len(Arbol.edges(nodo22)) == 1:
                    Arbol.remove_node(nodo22)
                

    n=0




print(CPC)

