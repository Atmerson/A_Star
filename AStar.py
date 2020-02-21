import math
import sys

# A star analysis
class AStar:
    """
    Graph Object includes A-Star evaluation and Heuristics.


    """

    def __init__(self, adjList, nodeLocations):
        self.adjList = adjList
        self.nodeLocations = nodeLocations


    def constraint(self, constraint):
        self.C = constraint

    # def setNodes(self, nodeCoords):
    #     self.nodeLocations = nodeCoords

    def neighbors(self, v: str) -> list:
        return self.adjList[v]

    def h(self, n: str) -> int:

        # heuristic is based on distance between current node to the goal node. no obstacles accounted for.

        nodes = self.nodeLocations.keys()

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
                                print('RESULTING PATH: '+ str(constraintPath))




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
