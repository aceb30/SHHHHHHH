import networkx as nx

Grafo = nx.Graph()
archivo = open("ProfesoraEncina.txt", "r")
cuantos = int(archivo.readline())

for n in range(0, cuantos):
    contactos = archivo.readline()
    separador= " "
    contactos = contactos.split(separador)
    entrenador = contactos[0]
    numerocontactos = int(contactos[1])
    desconfia = contactos[5]
    Grafo.add_node(entrenador)
    for m in range(0, numerocontactos):
        Grafo.add_edge(entrenador, contactos[m+2])


print(Grafo.nodes)
print(Grafo)

