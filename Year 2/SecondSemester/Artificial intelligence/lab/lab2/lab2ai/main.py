import string
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings

from pygmlparser.Parser import Parser
from pygmlparser.Graph import Graph
from pygmlparser.Edge import Edge
from pygmlparser.Node import Node
from pygmlparser.graphics.NodeGraphics import NodeGraphics
from pygmlparser.graphics.EdgeGraphics import EdgeGraphics
from pygmlparser.graphics.Point import Point


class Comunitate:
    def __init__(self, node, matrix):
        self.nodes = [node]
        self.edges = []
        self.matrix = matrix

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_matrix(self):
        return self.matrix

    def add_nodes_and_edges(self, new_nodes):
        for n in new_nodes:
            for nn in self.nodes:
                if self.matrix[n][nn] == 1:
                    self.edges.append((n, nn))
            self.nodes.append(n)

def parse(file: string):
    parser: Parser = Parser()
    parser.loadGML(file)
    parser.parse()
    graph: Graph = parser.graph
    return graph

def select_option(cmd: int):
    if cmd == 1:
        return parse('data/real/dolphins/dolphins.gml')
    elif cmd == 2:
        return parse('data/real/football/football.gml')
    elif cmd == 3:
        return parse('data/real/karate/karate.gml')
    elif cmd == 4:
        return parse('data/real/krebs/krebs.gml')
    elif cmd == 5:
        return parse('data/real/graph10.gml')
    elif cmd == 6:
        return parse('data/real/graph20.gml')
    elif cmd == 7:
        return parse('data/real/graph30.gml')
    elif cmd == 8:
        return parse('data/real/graph40.gml')
    elif cmd == 9:
        return parse('data/real/graph50.gml')
    elif cmd == 10:
        return parse('data/real/graph60.gml')

def adjacencyMatrix(graph: Graph):
    matrix = []
    nodes: Graph.Nodes = graph.graphNodes
    edges: Graph.Edges = graph.graphEdges
    for i in range (nodes.__len__()):
        matrix.append([])
        for j in range (nodes.__len__()):
            matrix[-1].append(0)

    for ed in edges:
        matrix[ed.source][ed.target] = 1
        matrix[ed.target][ed.source] = 1

    return matrix


def link_between_communities(com1, com2, edges):
    count = 0
    for edge in edges:
        if (edge.source in com1 and edge.target in com2) or (edge.source in com2 and edge.target in com1):
            count += 1
    return count


def nmb_edges_com(com1, edges):
    count = 0
    for edge in edges:
        if edge.source in com1 or edge.target in com1:
            count += 1
    return count


def find_communities(matrix, graph, nrc):
    comunities: list = list()
    nodes: Graph.Nodes = graph.graphNodes
    edges: Graph.Edges = graph.graphEdges
    for node in nodes:        com = Comunitate(node, matrix)
        comunities.append(com)
    while comunities.__len__() > nrc:
        maxi = -10000000
        comrez1 = None
        comrez2 = None
        for i in range(comunities.__len__()):
            for j in range(i+1, comunities.__len__()):
                nodesI = comunities[i].get_nodes()
                nodesJ = comunities[j].get_nodes()
                eij = link_between_communities(nodesI, nodesJ, edges)
                if eij > 0:
                    count1 = 0
                    count2 = 0
                    for edge in edges:
                        if edge.source in nodesI or edge.target in nodesI:
                            count1 += 1
                        if edge.source in nodesJ or edge.target in nodesJ:
                            count2 += 1

                    #ai = nmb_edges_com(comunities[i].get_nodes(), edges)
                    #aj = nmb_edges_com(comunities[j].get_nodes(), edges)
                    delta = 2 * (eij/edges.__len__() - (count1 * count2) /(edges.__len__() * edges.__len__()))
                    if delta > maxi:
                        maxi = delta
                        comrez1 = comunities[i]
                        comrez2 = comunities[j]

        comunities.remove(comrez2)
        comrez1.add_nodes_and_edges(comrez2.get_nodes())
    indici: list = list()
    for node in nodes:
        for com in range(comunities.__len__()):
            if node in comunities[com].get_nodes():
                indici.append(com)
                break
    return indici


def plotNetwork(network, communities=[1, 1, 1, 1, 1, 1]):
    np.random.seed(123)  # to freeze the graph's view (networks uses a random view)
    A = np.matrix(network)
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(15, 15))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()

def run(cmd, nrc):
    graph = select_option(cmd)
    matrix = adjacencyMatrix(graph)
    indici = find_communities(matrix, graph, nrc)
    for i in range (indici.__len__()):
        print(i+1, "    ", indici[i])
    plotNetwork(matrix,indici)


if __name__ == '__main__':
    print("1-dolphins")
    print("2-football")
    print("3-karate")
    print("4-krebs")
    print("5-Caz1")
    print("6-Caz2")
    print("7-Caz3")
    print("8-Caz4")
    print("9-Caz5")
    print("10-Caz6")

    cmd = input()
    print("number of communities:")
    nrC = input()
    run(int(cmd), int(nrC))
