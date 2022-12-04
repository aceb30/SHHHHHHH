import networkx as nx
import matplotlib
import pylab as plt
from networkx import minimum_spanning_tree

Grafo = nx.Graph()
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
    Grafo.add_edge(nodo1, nodo2, weight=2)


T = nx.minimum_spanning_tree(Grafo)
sorted(T.edges(data=True))

""""
nx.draw(Grafo, with_labels = True)
plt.savefig('Grafo2.3.png')
"""
""""
Arbol = minimum_spanning_tree(Grafo)
nx.draw(Arbol, with_labels = True)
plt.savefig('Arbol2.3.png')
"""

print(Grafo)
print(Grafo.edges)
print(T.edges)

R = nx.difference(Grafo, T)
print(R.edges)


A = nx.intersection(Grafo, T)
print(A.edges)

""""
Grafo.remove_edge("M2","N")

print(Grafo.edges)
"""
