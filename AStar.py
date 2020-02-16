import math
import sys

# A star analysis
class AStar:
    """
    Graph Object includes A-Star evaluation and Heuristics.


    """

    def __init__(self, adjList):
        self.adjList = adjList

        # for future application, populate the node locations.
        self.nodeLocations = {

            'A1': (2, 1),
            'A2': (2, 6),
            'A3': (17, 6),
            'A4': (17, 1),
            'B1': (1, 9),
            'B2': (0, 14),
            'B3': (6, 19),
            'B4': (9, 15),
            'B5': (7, 8),
            'C1': (10, 8),
            'C2': (12, 15),
            'C3': (14, 8),
            'D1': (14, 13),
            'D2': (14, 19),
            'D3': (18, 20),
            'D4': (20, 17),
            'E1': (19, 3),
            'E2': (18, 10),
            'E3': (23, 6),
            'F1': (22, 9),
            'F2': (22, 19),
            'F3': (28, 19),
            'F4': (28, 9),
            'G1': (28, 1),
            'G2': (25, 2),
            'G3': (25, 6),
            'G4': (29, 8),
            'G5': (31, 6),
            'G6': (31, 2),
            'H1': (32, 8),
            'H2': (29, 17),
            'H3': (31, 19),
            'H4': (34, 16),

            'START': (1, 3),
            'GOAL': (34, 19)
        }



    def constraint(self, constraint):
        self.C = constraint

    # def setNodes(self, nodeCoords):
    #     self.nodeLocations = nodeCoords

    def neighbors(self, v: str) -> list:
        return self.adjList[v]

    def h(self, n: str) -> int:

        # heuristic is based on distance between current node to the goal node. no obstacles accounted for.

        nodes = ['START', 'A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3',
                 'D4', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3', 'F4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'H1', 'H2', 'H3',
                 'H4', 'GOAL']

        H = {}
        for x in nodes:
            if x in self.nodeLocations:
                heuristic = dist((self.nodeLocations[x]), (34, 19))
                H[x] = heuristic

        return H[n]

    def analysis(self, startNode: str, goalNode: str):
        print('ANALYZING PATH FOR ' + startNode + ' NODE TO ' + goalNode + ' NODE')
        # list of nodes that have been visited but neighbors have not been visited.

        # list of nodes AND neighbors visited a
        # set returns a sorted list. (noice).
        closedList = set([])
        openList = set([startNode])

        g = {startNode: 0}  # the g dict contains the distance from the start node to other nodes.

        parents = {startNode: startNode}  # parents contains adjacency map of all nodes.

        currentCost = 0
        constraintPath =[]

        while len(openList) > 0:
            try:
                n = None
                for i in openList:
                    if n == None or g[i] + self.h(i) < g[n] + self.h(n):

                        n = i;


                        # N is the node we are going to evaluate.
                        # v is what we are checking in the open list

            except IndexError:
                pass

            if n == goalNode:
                newPath = []
                currentCost = 0
                while parents[n] != n:
                    newPath.append(n)

                    n = parents[n]




                newPath.append(startNode)

                newPath.reverse()

                for i in newPath:
                    for (v, weight) in self.neighbors(i):
                        if v in newPath:
                            currentCost = currentCost + weight




                            if currentCost > self.C:
                                print('COST EVALUATED: ' + str(currentCost))
                                print('GOAL NOT REACHED')




                                return constraintPath

                            else:
                                constraintPath.append(i)
                                continue

                print('COST EVALUATED: ' + str(currentCost))
                print('FINAL PATH FOUND: {}'.format(newPath))
                return newPath





                #print('FINAL PATH FOUND: {}'.format(newPath))

                #return newPath

            if n == None:
                print('NO PATH CONSTRUCTED.')
                return None

            for (v, weight) in self.neighbors(n):

                if v not in closedList and v not in openList:
                    openList.add(v)

                    parents[v] = n

                    g[v] = g[n] + weight


                else:
                    if g[v] > g[n] + weight:
                        g[v] = g[n] + weight
                        parents[v] = n

                        if v in closedList:
                            closedList.remove(v)
                            openList.add(v)

            openList.remove(n)
            closedList.add(n)



        print('NO PATH AVAILABLE')

        return None


def dist(start, target):
    return math.sqrt(((target[0] - start[0]) ** 2) + ((target[1] - start[1]) ** 2))
