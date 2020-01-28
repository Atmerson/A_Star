from collections import deque
import math

class Graph:

    def __init__(self, adjList):
        self.adjList = adjList

    def neighbors(self, v):
        return self.adjList[v]

    # why the fuck is the heuristic all 1?
    def h(self, n):
        H = {

            'A1': 1,
            'A2': 1,
            'A3': 1,
            'A4': 1,
            'B1': 1,
            'B2': 1,
            'B3': 1,
            'B4': 1,
            'B5': 1,
            'C1': 1,
            'C2': 1,
            'C3': 1,
            'D1': 1,
            'D2': 1,
            'D3': 1,
            'D4': 1,
            'E1':1,
            'E2':1,
            'E3':1,
            'F1':1,
            'F2':1,
            'F3':1,
            'F4':1,
            'G1':1,
            'G2':1,
            'G3':1,
            'G4':1,
            'G5':1,
            'G6':1,
            'H1':1,
            'H2':1,
            'H3':1,
            'H4':1,

            'START':1,
            'GOAL':0

        }

        return H[n]

    def a_star(self, startNode, goalNode):

        # list of nodes that have been visited but neighbors have not been visited.
        openList = set([startNode])  # set() basically returns a sorted list. sick

        # list of nodes AND neighbors visited a
        closedList = set([])

        # g contains current distances from start node to all other nodes.
        # will also always have the start node to begin with
        g = {startNode: 0}

        # parents contains adjacency map of all nodes.
        parents = {}
        parents[startNode] = startNode

        while len(openList) > 0:
            n = None

            # find a node with the lowest f() value

            for v in openList:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;  # N is the node we are going to evaluate.
                    # v is what we are checking in the open list


            if n == None:
                print('youre screwed bud')
                return None

            if n == goalNode:
                newPath = []

                while parents[n] != n:
                    newPath.append(n)
                    n = parents[n]

                newPath.append(startNode)

                newPath.reverse()

                print('LETS GOOO: {}'.format(newPath))

                return newPath

            # for all the neighbors in the current node do
            for (m, weight) in self.neighbors(n):

                if m not in openList and m not in closedList:
                    openList.add(m)

                    parents[m] = n
                    # g contains all the distances of the nodes.
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closedList:
                            closedList.remove(m)
                            openList.add(m)

            openList.remove(n)
            closedList.add(n)

        print('sorry bud')
        return None

def dist(start, target):

    return math.sqrt(((target[0] - start[0]) ** 2) + ((target[1] - start[1]) ** 2))


# adjacenyList = {
#     'START': [('A', dist((0,0),(19,19))), ('C', 2)],
#     'A': [('B', 10), ('C', 2)],
#     'B': [('D', 2), ('A', 10), ('E', 3), ('F', 90.8907)],
#     'C': [('D', 10), ('A', 2)],
#     'D': [('B', 2), ('C', 10)],
#     'E': [('G', 4), ('F', 4), ('B', 3)],
#     'F': [('FINISH', 5), ('G', 4), ('E', 4), ('B', 5)],
#     'G': [('FINISH', 7), ('F', 4), ('G', 4)],
#     'FINISH': [('G', 7), ('F', 5)]
#
# }




