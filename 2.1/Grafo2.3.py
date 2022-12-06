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

R = nx.difference(Grafo, T)
R = list(R.edges)

Arbol = Grafo.copy()

for n in range(0,len(R)):
    nodo1 = R[n][0]
    nodo2 = R[n][1]
    Arbol.remove_edge(nodo1, nodo2)


CPC=[]

while len(list(Arbol.nodes))!=0 and len(list(Arbol.edges))!=0:
    for nodo in list(Arbol.nodes):
        if len(Arbol.edges(nodo))==1:
            for edge in list(Arbol.edges):
                if edge[0] == nodo or edge[1] == nodo:
                    nodo1 = edge[0]
                    nodo2 = edge[1]
                    if nodo1 == nodo:
                        nodo11 = nodo1
                        nodo22 = nodo2
                    if nodo2 == nodo:
                        nodo11 = nodo2
                        nodo22 = nodo1

                    CPC.append([nodo1, nodo2])
                    try:
                        Arbol.remove_edge(nodo1, nodo2)
                    except:
                        pass
                    try:
                        Arbol.remove_node(nodo)
                    except:
                        pass
                    try:
                        Arbol.remove_node(nodo11)
                    except:
                        pass

                    if len(Arbol.edges(nodo22)) <= 2:
                        Arbol.remove_node(nodo22)

if len(list(Arbol.nodes))!=0:
    nodo = (list(Arbol.nodes))
    edges = list(Grafo.edges(nodo[0]))
    CPC.append([edges[0][0],edges[0][1]])
    print(CPC)
