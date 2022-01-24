import pygame
import random
import time


SCREEN_SIZE = (600, 600)
BLACK, RED, GREEN, WHITE = (0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 255, 255)
WAIT_TIME = 0.05


class selection_sort_visuliser:
    def __init__(self, ls):
        self.list = ls
        self.sorted_list = []

        pygame.init()
        self.window = pygame.display.set_mode(SCREEN_SIZE)

    def sort(self):
        for i in range(len(self.list)):
            time.sleep(WAIT_TIME) 
            self.draw_boxes()

            min = 0
            inx = 0
            for j, k in enumerate(self.list):
                if k < min or min == 0:
                    min = k
                    inx = j

            self.sorted_list.append(min)
            self.list.pop(inx)

        self.draw_boxes()

    def draw_boxes(self):
        self.window.fill(BLACK)

        l1 = [i for i in self.list]
        l2 = [i for i in self.sorted_list]

        for i in l1:
            l2.append(i)

        for i, x in enumerate(l2):
            pygame.draw.rect(self.window, self.check_pos(i, l2), (i * 10, SCREEN_SIZE[1] - x, 10, x))
            pygame.draw.rect(self.window, BLACK, (i * 10, SCREEN_SIZE[1] - x, 10, x), 5)

        pygame.display.update()

    def check_pos(self, index, ls):
        for i in range(0, index):
            if ls[i] > ls[index]:
                return RED

        for i in range(index, len(self.list)):
            if self.list[i] < self.list[index]:
                return WHITE

        return GREEN

    def event_handeler(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    main()


def main():
    s = selection_sort_visuliser([random.randint(10, SCREEN_SIZE[1] - 50) for _ in range(SCREEN_SIZE[0] // 10)])
    s.sort()
    s.event_handeler()


main()