import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
name_dict = dict()

with open("ProfesoraEncina.txt") as f:
    trainer_cnt = int(f.readline())
    
    for n in range(0, trainer_cnt):
        trainer_data = f.readline().split(' ')
        
        name = trainer_data[0]
        g.add_node(name)
        
        for o in range(0, int(trainer_data[1])):
            g.add_node(trainer_data[o + 2])
            g.add_edge(name, trainer_data[o + 2])
        
        name_dict[name] = "yes" in trainer_data[int(trainer_data[1]) + 2]

for node in list(g.nodes):
    if name_dict[node]:
        for edge in list(g.edges):
            if edge[1] == node and (edge[1], edge[0]) not in list(g.edges):
                g.remove_edge(edge[0], edge[1])

for f in nx.kosaraju_strongly_connected_components(g):
    print(list(f)[0])
