import pygame
import sys
import math
import thorpy
from AStar import AStar
from Node import PathCoords


# TODO Condense adjaceny list.

def adjustCoordinates(x, y):
    newX = (20 * x)
    newY = 400 - (20 * y)

    return (newX, newY)


def dist(start, target):
    return math.sqrt(((target[0] - start[0]) ** 2) + ((target[1] - start[1]) ** 2))


# NODE : (NEIGHBOR, COST/DISTANCE TO GET THERE)

# this adj list couldve also been automated but it doesnt know its immediate neighbors.
# maybe easier for a randomly generated environment.



####MAIN EVENT#####

# Feed Env to A star. State start and target.
def main():
    env1 = {
        'START': [('A1', dist((1, 3), (2, 1))), ('A2', dist((1, 3), (2, 6))), ('B1', dist((1, 3), (1, 9))),
                  ('B2', dist((1, 3), (0, 14)))],
        'A1': [('A2', 5), ('A4', 15), ('B1', dist((2, 1), (1, 9))), ('B2', dist((2, 1), (0, 14)))],
        'A2': [('A1', 5), ('A3', 15), ('B1', dist((2, 6), (1, 9))), ('B5', dist((2, 6), (7, 8))),
               ('C1', dist((2, 6), (10, 8))), ('C3', dist((2, 6), (14, 8)))],
        'A3': [('A2', 15), ('A4', 5), ('C1', dist((17, 6), (10, 8))), ('C3', dist((17, 6), (14, 8))),
               ('C2', dist((17, 6), (12, 15))), ('D1', dist((17, 6), (14, 13))), ('E2', dist((17, 6), (18, 10))),
               ('B5', dist((17, 6), (7, 8)))],
        'A4': [('A3', 5), ('A1', 15), ('E1', dist((17, 1), (19, 3))), ('E2', dist((17, 1), (18, 10))),
               ('G2', dist((17, 1), (25, 2))), ('G3', dist((17, 1), (25, 6))), ('G1', dist((17, 1), (28, 1)))],
        'B1': [('A2', dist((1, 9), (2, 6))), ('B2', dist((1, 9), (0, 14))), ('B5', dist((1, 9), (7, 8)))],
        'B2': [('B1', dist((0, 14), (1, 9))), ('B3', dist((0, 14), (6, 19))), ('A1', dist((0, 14), (2, 1)))],
        'B3': [('B2', dist((6, 19), (0, 14))), ('B4', dist((6, 19), (9, 15))), ('D2', dist((6, 19), (14, 19))),
               ('D3', dist((6, 19), (18, 20))), ('C2', dist((6, 19), (12, 15)))],
        'B4': [('B3', dist((9, 15), (6, 19))), ('B5', dist((9, 15), (7, 8))), ('C2', dist((9, 15), (12, 15))),
               ('C2', dist((9, 15), (10, 8)))],
        'B5': [('B1', dist((7, 8), (1, 9))), ('B4', dist((7, 8), (9, 15))), ('C1', 5), ('C2', dist((7, 8), (12, 15)))],
        'C1': [('C2', dist((10, 8), (12, 15))), ('C3', 4), ('A2', dist((2, 6), (10, 8))),
               ('A3', dist((17, 6), (10, 8))),
               ('B5', 3)],
        'C2': [('C1', dist((10, 8), (12, 15))), ('C3', dist((12, 15), (14, 8))), ('B3', dist((6, 19), (12, 15))),
               ('B4', 3),
               ('D2', dist((14, 19), (12, 15))), ('D1', dist((12, 15), (14, 13)))],
        'C3': [('C1', 3), ('C2', dist((12, 15), (14, 8))), ('A2', dist((2, 6), (14, 8))),
               ('A3', dist((17, 6), (14, 8))),
               ('E2', dist((14, 8), (18, 10))), ('D1', dist((14, 13), (14, 8)))],
        'D1': [('D2', dist((14, 13), (14, 19))), ('D4', dist((14, 13), (20, 17))), ('C2', dist((12, 15), (14, 13))),
               ('C3', dist((14, 13), (14, 8))), ('A3', dist((17, 6), (14, 13))), ('E2', dist((14, 13), (18, 10))),
               ('F1', dist((14, 13), (22, 9)))],
        'D2': [('D1', dist((14, 13), (14, 19))), ('D3', dist((14, 19), (18, 20))), ('C2', dist((14, 19), (12, 15))),
               ('B3', dist((6, 19), (14, 19)))],
        'D3': [('D4', dist((18, 20), (20, 17))), ('D2', dist((18, 20), (14, 19))), ('F2', dist((18, 20), (22, 19))),
               ('B3', dist((6, 19), (18, 20)))],
        'D4': [('D3', dist((18, 20), (20, 17))), ('D1', dist((14, 13), (20, 17))), ('F2', dist((20, 17), (22, 19))),
               ('E2', dist((20, 17), (18, 10))), ('F1', dist((20, 17), (22, 9)))],
        'E2': [('E1', dist((18, 10), (19, 3))), ('E3', dist((18, 10), (23, 6))), ('F1', dist((18, 10), (22, 9))),
               ('F2', dist((18, 10), (22, 19))), ('D4', dist((18, 10), (20, 17))), ('D1', dist((18, 10), (14, 13))),
               ('C3', dist((18, 10), (14, 8))), ('A3', dist((18, 10), (17, 6))), ('A4', dist((18, 10), (17, 1)))],
        'E1': [('E2', dist((19, 3), (18, 10))), ('E3', dist((19, 3), (23, 6))), ('A3', dist((19, 3), (17, 6))),
               ('A4', dist((19, 3), (17, 1))), ('G1', dist((19, 3), (28, 1))), ('G2', dist((19, 3), (25, 2))),
               ('G3', dist((19, 3), (25, 6))), ('F4', dist((19, 3), (28, 9)))],
        'E3': [('E2', dist((18, 10), (23, 6))), ('E1', dist((19, 3), (23, 6))), ('F1', dist((23, 6), (22, 9))),
               ('F4', dist((23, 6), (28, 9))), ('G4', dist((29, 8), (23, 6))), ('G3', dist((25, 6), (23, 6))),
               ('G2', dist((23, 6), (25, 2)))],
        'F1': [('F2', 10), ('F4', 6), ('D4', dist((20, 17), (22, 9))), ('E2', dist((18, 10), (22, 9))),
               ('E3', dist((23, 6), (22, 9))), ('G3', dist((25, 6), (22, 9))), ('G4', dist((22, 9), (29, 8)))],
        'F2': [('F3', 6), ('F1', 10), ('D3', dist((18, 20), (22, 19))), ('D4', dist((20, 17), (22, 19)))],
        'F3': [('F2', 6), ('F4', 10), ('H2', dist((28, 19), (29, 17))), ('H3', dist((28, 19), (31, 19)))],
        'F4': [('F1', 6), ('F2', 10), ('H2', dist((28, 9), (29, 17))), ('H1', dist((32, 8), (28, 9))),
               ('G4', dist((28, 9), (29, 8))), ('G3', dist((28, 9), (25, 6))), ('E3', dist((23, 6), (28, 9)))],
        'G1': [('G2', dist((28, 1), (25, 2))), ('G6', dist((31, 2), (28, 1))), ('A4', 11)],
        'G2': [('G1', dist((28, 1), (25, 2))), ('G3', dist((25, 6), (25, 2))), ('E1', dist((19, 3), (25, 2))),
               ('E3', dist((23, 6), (25, 2))), ('A4', dist((17, 1), (25, 2)))],
        'G3': [('G2', 4), ('G4', dist((25, 6), (29, 8))), ('E3', dist((25, 6), (23, 6))),
               ('E1', dist((25, 6), (19, 3))),
               ('A4', dist((17, 1), (25, 6)))],
        'G4': [('G3', dist((29, 8), (25, 6))), ('G5', dist((31, 6), (29, 8))), ('F4', dist((28, 9), (29, 8))),
               ('G4', dist((22, 9), (29, 8))), ('E3', dist((29, 8), (23, 6))), ('H1', dist((32, 8), (29, 8))),
               ('H2', dist((29, 8), (29, 17)))],
        'G5': [('G4', dist((29, 8), (31, 6))), ('G6', 4), ('H1', dist((32, 8), (31, 6)))],
        'G6': [('G5', 4), ('G1', dist((28, 1), (31, 2)))],
        'H1': [('G5', dist((32, 8), (31, 6))), ('H2', dist((29, 17), (32, 8))), ('H4', dist((34, 16), (32, 8))),
               ('F4', dist((32, 8), (28, 9))), ('G4', dist((32, 8), (29, 8)))],
        'H2': [('H1', dist((29, 17), (32, 8))), ('H3', dist((31, 19), (29, 17))), ('F3', dist((28, 19), (29, 17))),
               ('F4', dist((28, 9), (29, 17))), ('G4', dist((29, 8), (29, 17)))],
        'H3': [('H2', dist((31, 19), (29, 17))), ('H4', dist((31, 19), (34, 16))), ('F3', 3),
               ('GOAL', dist((31, 19), (34, 19)))],
        'H4': [('H1', dist((34, 16), (32, 8))), ('H3', dist((31, 19), (34, 16))), ('GOAL', dist((34, 19), (34, 16)))],
        'GOAL': [('H4', dist((34, 19), (34, 16))), ('H3', dist((31, 19), (34, 19)))]

    }

    env1coords = {

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
    # fill this bad boi up
    env2 = {
        'A1': [('A2', dist((7, 8), (10, 8))), ('A3', dist((7, 8), (9, 15))), ('C1', dist((7, 8), (2, 6))),
               ('E1', dist((6, 19), (7, 8)))],
        'A2': [('A1', dist((10, 8), (7, 8))), ('A3', dist((10, 8), (9, 15))), ('E3', dist((12, 15), (10, 8))),
               ('B3', dist((14, 13), (10, 8))), ('B1', dist((14, 8), (10, 8))), ('C1', dist((2, 6), (10, 8))),
               ('C3', dist((23, 6), (10, 8)))],
        'A3': [('A1', dist((9, 15), (7, 8))), ('A2', dist((9, 15), (10, 8))), ('E3', 3), ('E1', dist((6, 19), (9, 15))),
               ('B3', dist((9, 15), (14, 13))), ('B1', dist((9, 15), (14, 8))), ('C1', dist((2, 6), (9, 15)))],
        'B1': [('A2', 4), ('B3', dist((14, 13), (14, 8))), ('B2', dist((22, 10), (14, 8))),
               ('A3', dist((9, 15), (14, 8))),
               ('E3', dist((12, 15), (14, 8))), ('C1', dist((2, 6), (14, 8))), ('C3', dist((23, 6), (14, 8)))],
        'B2': [('B1', dist((22, 10), (14, 8))), ('B3', dist((22, 10), (14, 13))), ('C3', dist((22, 10), (23, 6))),
               ('D1', dist((25, 6), (22, 10))), ('E2', dist((20, 17), (22, 10))), ('D3', dist((28, 19), (22, 10)))],
        'B3': [('B1', 5), ('B2', dist((14, 8), (22, 10))), ('E3', dist((12, 15), (14, 13))),
               ('A2', dist((14, 13), (10, 8))), ('A3', dist((9, 15), (14, 13))), ('E2', dist((20, 17), (14, 13))),
               ('D3', dist((28, 19), (14, 13)))],
        'C1': [('C2', dist((2, 6), (17, 1))), ('C3', 21), ('A1', dist((2, 6), (7, 8))), ('A2', dist((2, 6), (10, 8))),
               ('B1', dist((14, 8), (2, 6))), ('E1', dist((2, 6), (6, 19)))],
        'C2': [('C1', dist((17, 1), (2, 6))), ('C3', dist((17, 1), (23, 6))), ('D1', dist((25, 6), (17, 1)))],
        'C3': [('C2', dist((23, 6), (17, 1))), ('C1', dist((23, 6), (2, 6))), ('B2', dist((23, 6), (22, 10))),
               ('D3', dist((28, 19), (23, 6))), ('D1', 2), ('B1', dist((23, 6), (14, 8))),
               ('A2', dist((10, 8), (23, 6))),
               ('A2', dist((23, 6), (10, 8)))],
        'D1': [('D2', dist((25, 6), (32, 8))), ('D3', dist((25, 6), (28, 19))), ('B2', dist((22, 10), (25, 6))),
               ('C3', 2),
               ('C2', dist((17, 1), (25, 6)))],
        'D2': [('D1', dist((25, 6), (32, 8))), ('D3', dist((28, 19), (32, 8))), ('C2', dist((17, 1), (32, 8))),
               ('GOAL', dist((32, 8), (34, 10)))],
        'D3': [('D2', dist((28, 19), (32, 8))), ('D1', dist((25, 6), (28, 19))), ('E2', dist((20, 17), (28, 19))),
               ('B2', dist((22, 10), (28, 19))), ('C3', dist((28, 19), (23, 6))), ('GOAL', dist((28, 19), (34, 10)))],
        'E1': [('E2', dist((20, 17), (6, 19))), ('E3', dist((12, 15), (6, 19))), ('A3', dist((9, 15), (6, 19))),
               ('A1', dist((6, 19), (7, 8))), ('C1', dist((6, 19), (2, 6)))],
        'E2': [('E1', dist((20, 17), (6, 19))), ('E3', dist((12, 15), (20, 17))), ('D3', dist((28, 19), (20, 17))),
               ('B2', dist((20, 17), (22, 10))), ('B3', dist((20, 17), (14, 13)))],
        'E3': [('E1', dist((12, 15), (6, 19))), ('E2', dist((12, 15), (20, 17))), ('A3', 3),
               ('B3', dist((14, 13), (12, 15))), ('B1', dist((14, 18), (12, 15))), ('A2', dist((12, 15), (10, 8))),
               ('D3', dist((28, 19), (12, 15)))],
        'START': [('C1', dist((2, 6), (2, 14))), ('A1', dist((7, 8), (2, 14))), ('A3', dist((9, 15), (2, 14))),
                  ('E1', dist((6, 19), (2, 14)))],
        'GOAL': [('D3', dist((28, 19), (34, 10))), ('D2', dist((32, 8), (34, 10)))]

    }

    env2coords = {
        'A1': (7, 8),
        'A2': (10, 8),
        'A3': (9, 15),
        'B1': (14, 8),
        'B2': (22, 10),
        'B3': (14, 13),
        'C1': (2, 6),
        'C2': (17, 1),
        'C3': (23, 6),
        'D1': (25, 6),
        'D2': (32, 8),
        'D3': (28, 19),
        'E1': (6, 19),
        'E2': (20, 17),
        'E3': (12, 15),
        'START': (2, 14),
        'GOAL': (34, 10)
    }

    print('Enter Cost Constraint: ')
    costConstraint = input()
    print('Enter 1 or 2 for Environments: ')
    pygame.init()

    window = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    screen = pygame.display.set_mode((800, 400), window)
    backgroundColor = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    done = False
    environment = 0
    clock = pygame.time.Clock()

    pygame.display.set_caption('A STAR')

    pygame.draw.polygon(screen, BLACK, [adjustCoordinates(7, 8), adjustCoordinates(10, 8), adjustCoordinates(9, 15)])


    ###### INPUT BOX TEST ######


    while not done:
        events = pygame.event.get()
        screen.fill(backgroundColor)


        for event in events:
            if event.type == pygame.QUIT:
                return

                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    environment = 1
                    EnvAnalysis = AStar(env1, env1coords)
                    EnvAnalysis.constraint(int(costConstraint))
                    newPath = EnvAnalysis.analysis('START', 'GOAL')

                    # Convert path to PyGame coordinates for mapping.
                    convertPath = PathCoords(newPath, env1coords)
                    coordinateList = convertPath.convertCoordinates()



                elif event.key == pygame.K_2:

                    environment = 2
                    EnvAnalysis2 = AStar(env2, env2coords)
                    EnvAnalysis2.constraint(int(costConstraint))
                    newPath = EnvAnalysis2.analysis('START', 'GOAL')

                    # Convert path to PyGame coordinates for mapping.
                    convertPath = PathCoords(newPath, env2coords)
                    coordinateList = convertPath.convertCoordinates()

                elif event.key == pygame.K_ESCAPE:
                    return


        if environment == 1:

            pygame.draw.circle(screen, GREEN, adjustCoordinates(1, 3), 8)
            pygame.draw.circle(screen, GREEN, adjustCoordinates(34, 19), 8)

            # Rectangle
            pygame.draw.polygon(screen, BLACK, [adjustCoordinates(2,6),adjustCoordinates(17,6),adjustCoordinates(17,1),adjustCoordinates(2,1)],3)

            # Pentagon

            pygame.draw.polygon(screen, BLACK, [adjustCoordinates(0,14),adjustCoordinates(6,19),adjustCoordinates(9,15),adjustCoordinates(7,8),adjustCoordinates(1,9),adjustCoordinates(0,14)],3)

            # Triangle
            pygame.draw.polygon(screen,BLACK, [adjustCoordinates(10,8),adjustCoordinates(14,8),adjustCoordinates(12,15)],3)


            # Quadri
            pygame.draw.polygon(screen,BLACK, [adjustCoordinates(14,19),adjustCoordinates(18,20),adjustCoordinates(20,17),adjustCoordinates(14,13)],3)


            # Triangle
            pygame.draw.polygon(screen,BLACK,[adjustCoordinates(18,10),adjustCoordinates(23,6),adjustCoordinates(19,3)],3)


            # F TANGLE
            pygame.draw.polygon(screen,BLACK, [adjustCoordinates(22,19),adjustCoordinates(28,19),adjustCoordinates(28,9),adjustCoordinates(22,9)],3)


            # HEX
            pygame.draw.polygon(screen,BLACK, [adjustCoordinates(29,8),adjustCoordinates(31,6),adjustCoordinates(31,2),adjustCoordinates(28,1),adjustCoordinates(25,2),adjustCoordinates(25,6)],3)


            # H LATERAL
            pygame.draw.polygon(screen,BLACK, [adjustCoordinates(31,19),adjustCoordinates(34,16),adjustCoordinates(32,8),adjustCoordinates(29,17)],3)


            for i in coordinateList:
                pygame.draw.line(screen, GREEN, i[0], i[1], 3)

        # PATH
        elif environment == 2:

            # A
            pygame.draw.polygon(screen, BLACK,
                                [adjustCoordinates(7, 8), adjustCoordinates(10, 8), adjustCoordinates(9, 15)], 3)

            # B
            pygame.draw.polygon(screen, BLACK,
                                [adjustCoordinates(14, 8), adjustCoordinates(14, 13), adjustCoordinates(22, 10)], 3)

            # C
            pygame.draw.polygon(screen, BLACK,
                                [adjustCoordinates(2, 6), adjustCoordinates(17, 1), adjustCoordinates(23, 6)], 3)
            # for i in coordinateList:

            # D
            pygame.draw.polygon(screen, BLACK,
                                [adjustCoordinates(28, 19), adjustCoordinates(25, 6), adjustCoordinates(32, 8)], 3)
            #     pygame.draw.line(screen, GREEN, i[0], i[1], 3)

            # E
            pygame.draw.polygon(screen, BLACK,
                                [adjustCoordinates(6, 19), adjustCoordinates(20, 17), adjustCoordinates(12, 15)], 3)

            pygame.draw.circle(screen, GREEN, adjustCoordinates(2, 14), 8)
            pygame.draw.circle(screen, GREEN, adjustCoordinates(34, 10), 8)

            for i in coordinateList:
                pygame.draw.line(screen, GREEN, i[0], i[1], 3)

        pygame.display.update()
        pygame.display.flip()

    pygame.display.quit()

running = True


while running:

    main()
    print('Run again? y/n')
    userResponse = input()
    if userResponse == 'y':
        main()
    else:
        running == False
        sys.exit()




#TODO: wrap everthing in a main function.