import sys
import itertools


# Coordinate manipulation and conversion.
# 800 x 400 pygame size
class PathCoords:
    def __init__(self, PathList, nodeLocations):
        self.pathlist = PathList
        self.nodeLocations = nodeLocations
        # self.nodeLocations = {
        #     'A1': (2, 1),
        #     'A2': (2, 6),
        #     'A3': (17, 6),
        #     'A4': (17, 1),
        #     'B1': (1, 9),
        #     'B2': (0, 14),
        #     'B3': (6, 19),
        #     'B4': (9, 15),
        #     'B5': (7, 8),
        #     'C1': (10, 8),
        #     'C2': (12, 15),
        #     'C3': (14, 8),
        #     'D1': (14, 13),
        #     'D2': (14, 19),
        #     'D3': (18, 20),
        #     'D4': (20, 17),
        #     'E1': (19, 3),
        #     'E2': (18, 10),
        #     'E3': (23, 6),
        #     'F1': (22, 9),
        #     'F2': (22, 19),
        #     'F3': (28, 19),
        #     'F4': (28, 9),
        #     'G1': (28, 1),
        #     'G2': (25, 2),
        #     'G3': (25, 6),
        #     'G4': (29, 8),
        #     'G5': (31, 6),
        #     'G6': (31, 2),
        #     'H1': (32, 8),
        #     'H2': (29, 17),
        #     'H3': (31, 19),
        #     'H4': (34, 16),
        #
        #     'START': (1, 3),
        #     'GOAL': (34, 19)
        # }

    def convertCoordinates(self):
        coordList = [self.nodeLocations[i] for i in self.pathlist]

        graphPath = []
        index = 1
        for x in coordList:

            try:
                endpoint = coordList[index]
                X0 = (20 * x[0])
                Y0 = 400 - (20 * x[1])
                X1 = (20 * endpoint[0])
                Y1 = 400 - (20 * endpoint[1])
                graphPairs = ((X0, Y0), (X1, Y1))
                graphPath.append(graphPairs)
                index = index + 1

            except IndexError:
                pass

        return graphPath
