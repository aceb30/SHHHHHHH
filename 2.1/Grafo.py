import networkx as nx

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
    costo= int(arista[2])
    Grafo.add_edge(nodo1, nodo2, weight=costo)

pasos = int(archivo.readline())
ni = archivo.readline()
ni=ni[:-1]
camino = []
for n in range(0,pasos):
    nf_aux = archivo.readline()
    if nf_aux=="":
        break

    nf = nf_aux[:-1]
    camino+=nx.dijkstra_path(Grafo, ni, nf)
    camino.pop()
    ni = nf

camino+=nx.dijkstra_path(Grafo, nf, "L1")

print(camino)





















