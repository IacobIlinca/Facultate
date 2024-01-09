from fcOptimisation.RealChromosome import *
from lab2 import *
import string
import os
import numpy as np
from random import seed
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import warnings

from pygmlparser.Parser import Parser
from pygmlparser.Graph import Graph


def createNetwork(file):
    graph: Graph = parse(file)
    n = graph.graphNodes.__len__()
    matrix = adjacencyMatrix(graph)
    net = {}
    net['noNodes'] = n
    net["mat"] = matrix
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (matrix[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += matrix[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    return net


def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M


def num_connected_components(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    visited = [False] * noNodes
    num_components = 0
    for i in range(0, noNodes):
        if not visited[i]:
            dfs(i, visited, mat, communities)
            num_components += 1
    return num_components


def dfs(node, visited, mat, communities):
    visited[node] = True
    for neighbor in range(0, len(mat)):
        if mat[node][neighbor] == 1 and not visited[neighbor] and communities[neighbor] == communities[node]:
            dfs(neighbor, visited, mat, communities)


def modularity_conductance(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']

    total_conductance = 0.0
    for i in range(0, noNodes):
        # Calculate the conductance of each community
        community_nodes = [j for j in range(noNodes) if communities[j] == communities[i]]
        boundary_edges = [mat[i][j] for j in range(noNodes) if communities[j] != communities[i]]
        boundary_nodes = [j for j in range(noNodes) if communities[j] != communities[i]]

        internal_degree = sum([degrees[j] for j in community_nodes])
        external_degree = sum(boundary_edges)
        community_conductance = external_degree / (internal_degree + external_degree)

        # Add the conductance to the total modularity score
        total_conductance += community_conductance

    # Return the average conductance over all communities
    return 1 - (total_conductance / noNodes)


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        self.__probs = []
        self.__fitnesses = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
            self.__fitnesses.append(0)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam['network'])

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        poz = 0
        for i in range (0,self.__population.__len__()):
            if self.__population[i].fitness < best.fitness:
                best = self.__population[i]
                poz = i
        return best, poz

    def probsAndFitness(self):
        for i in range (0, self.__param['popSize']):
            self.__fitnesses[i] = self.__population[i].fitness + 1
        tot_fit = sum(self.__fitnesses)
        self.__probs = np.array(self.__fitnesses) / tot_fit

    def selection(self):
        parent = np.random.choice(len(self.__fitnesses), size=1, replace=False, p=self.__probs)
        return parent[0]

    def oneGeneration(self):
        newPop = []
        self.probsAndFitness()
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        self.probsAndFitness()
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres, self.__problParam['network'])
            worst = self.worstChromosome()
            if off.fitness > worst[0].fitness:
                self.__population[worst[1]] = off
                self.probsAndFitness()


class Generator:

    def __init__(self, path, noGen, nrC, modularity, popSize):
        self.__path = path
        self.__noGen = noGen
        self.__nrC = nrC
        self.__network = createNetwork(path)

        self.__gaParam = {'popSize': popSize, 'noGen': self.__noGen}
        self.__problParam = {'min':1, 'max': nrC, 'function': modularity ,'noDim': self.__network['noNodes'], 'network': self.__network}

        self.__ga = GA(self.__gaParam, self.__problParam)

    def start(self):
        self.__ga.initialisation()
        self.__ga.evaluation()
        self.__ga.probsAndFitness()

        the_best_chr = []
        bests = []

        for g in range(self.__gaParam['noGen']):
            #self.__ga.oneGeneration()
            #self.__ga.oneGenerationElitism()
            self.__ga.oneGenerationSteadyState()

            bestChromo = self.__ga.bestChromosome()
            bests.append(bestChromo.fitness)
            print(g)
            the_best_chr.append(bestChromo)


        plt.plot(bests)
        the_best_chr.sort(reverse=True)
        plotNetwork(self.__network['mat'], the_best_chr[0].repres)


if __name__ == '__main__':
    print("1-dolphins")
    print("2-football")
    print("3-karate")
    print("4-krebs")
    print("5-Caz1")
    print("6-Caz2")
    print("7-Caz3")
    print("8-Caz4")
    #cmd = input()

    nrC = 2
    #gen = Generator('real-networks/real/dolphins/dolphins.gml', 50, 2, modularity, 100)
    gen = Generator('real-networks/real/netscience.gml', 1, 2, modularity, 100)
    #gen = Generator('real-networks/real/lesmis.gml', 50, 2, modularity, 100)
    #gen = Generator('real-networks/real/football/football.gml', 100, 2, modularity, 100)
    #gen = Generator('real-networks/real/karate/karate.gml', 100, 2, num_connected_components, 100)
    #gen = Generator('real-networks/real/krebs/krebs.gml', 100, 2, modularity, 100)
    #gen = Generator('real-networks/real/graph10.gml', 100, 2, modularity, 100)
    #gen = Generator('real-networks/real/graph20.gml', 100, 2, modularity, 100)
    #gen = Generator('real-networks/real/graph30.gml', 100, 2, modularity, 100)
    #gen = Generator('real-networks/real/graph40.gml', 100, 2, modularity, 100)

    gen.start()
