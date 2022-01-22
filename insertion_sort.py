import pygame
import random
import sys
import time


sys.setrecursionlimit(1500)


NUM = 60
SCREEN_SIZE = (600, 600)
BLACK, RED, GREEN = (0, 0, 0), (255, 0, 0), (0, 255, 0)
WAIT_TIME = 0


class visulise_insertion_sort:
    def __init__(self, ls):
        self.list = ls

        pygame.init()
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.update()

    def draw_boxes(self):
        self.window.fill(BLACK)

        for i, x in enumerate(self.list):
            pygame.draw.rect(self.window, self.check_pos(i), (i * 10, SCREEN_SIZE[1] - x, 10, x))
            pygame.draw.rect(self.window, BLACK, (i * 10, SCREEN_SIZE[1] - x, 10, x), 5)

        time.sleep(WAIT_TIME)

        pygame.display.update()

    def check_pos(self, index):
        for i in range(0, index):
            if self.list[i] > self.list[index]:
                return RED

        return GREEN

    def sort_visulise(self):
        for i, x in enumerate(self.list):
            if i > 0:
                if x < self.list[i - 1]:
                    self.list[i], self.list[i - 1] = self.list[i - 1], x
                    self.draw_boxes()
                    self.sort_visulise()
                    return

        self.event_handeler()

    def event_handeler(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    return


def main():
    ls = [random.randint(10, SCREEN_SIZE[1] - 50) for _ in range(SCREEN_SIZE[0] // 10)]

    v = visulise_insertion_sort([i for i in ls])
    v.sort_visulise()


while True:
    main()