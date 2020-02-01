import math


# A star analysis
class Graph:
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

    def a_star(self, startNode: str, goalNode: str):
        print('ANALYZING PATH FOR ' + startNode + ' NODE TO ' + goalNode + ' NODE')
        # list of nodes that have been visited but neighbors have not been visited.
        openList = set([startNode])  # set() basically returns a sorted list. sick

        # list of nodes AND neighbors visited a
        closedList = set([])

        # g contains current distances from start node to all other nodes.
        # will also always have the start node to begin with
        g = {startNode: 0}

        # parents contains adjacency map of all nodes.
        parents = {startNode: startNode}

        while len(openList) > 0:
            n = None

            # find a node with the lowest f() value

            for v in openList:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;
                    # N is the node we are going to evaluate.
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

                print('FINAL PATH FOUND: {}'.format(newPath))
                print(closedList)
                print(openList)
                print(g)
                return newPath

            # for all the neighbors in the current node do
            for (m, weight) in self.neighbors(n):

                # goes around the node and adds its neigbors to the open list.
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

        print('NO PATH AVAILABLE')

        return None


def dist(start, target):
    return math.sqrt(((target[0] - start[0]) ** 2) + ((target[1] - start[1]) ** 2))
