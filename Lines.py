import pygame

TIME = 0
BLUE = (30,30,30)
class AnimateLines:

    def __init__(self,coordinates,speed, color = BLUE):
        self.points = coordinates
        self.pixelcount = len(self.points)
        self.speed = speed
        self.start = coordinates[0]
        self.end = coordinates[1]
        self.currentPixel = 0
        self.latestUpdate = 0
        self.drawn = False
        self.color = color


    def update(self):
        global TIME


        if self.drawn is True:
            pass

        else:

            if self.latestUpdate == 0:
                self.latestUpdate = TIME
                time_changed = 0

            else:
                time_changed = TIME - self.latestUpdate
                self.latestUpdate = TIME

            new_pixels = time_changed * self.speed / 1000

            if new_pixels + self.currentPixel > self.pixelcount:
                self.end = self.points[-1]
                self.drawn = True

            else:

                self.currentPixel += new_pixels
                self.end = self.points[int(self.currentPixel)]



    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, 4)

