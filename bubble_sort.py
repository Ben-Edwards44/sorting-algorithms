import random
import pygame
import time


SCREEN_SIZE = (600, 600)
WHITE, BLACK, GREEN, RED, WHITE = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255)
WAIT_TIME = 0


class bubble_sort_visulisation:
    def __init__(self, ls):
        pygame.init()
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.update()

        self.list = ls

    def draw_boxes(self):
        self.window.fill(BLACK)

        for i, x in enumerate(self.list):
            pygame.draw.rect(self.window, self.check_pos(i), (i * 10, SCREEN_SIZE[1] - x, 10, x))
            pygame.draw.rect(self.window, BLACK, (i * 10, SCREEN_SIZE[1] - x, 10, x), 5)

        pygame.display.update()

    def check_pos(self, index):
        for i in range(0, index):
            if self.list[i] > self.list[index]:
                return RED

        for i in range(index, len(self.list)):
            if self.list[i] < self.list[index]:
                return WHITE

        return GREEN

    def main_visulise(self):
        for i, x in enumerate(self.list):
            if i < len(self.list) - 1:
                if x > self.list[i + 1]:
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
                    self.draw_boxes()

        time.sleep(WAIT_TIME)

        if not self.check():
            self.main_visulise()

    def check(self):
        for i, x in enumerate(self.list):
            if i < len(self.list) - 1:
                if x > self.list[i + 1]:
                    return False

        return True

    def event_handeler(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    main()


def main():
    ls = [random.randint(10, SCREEN_SIZE[1] - 50) for _ in range(SCREEN_SIZE[0] // 10)]
    sorter = bubble_sort_visulisation([i for i in ls])
    sorter.draw_boxes()
    sorter.main_visulise()
    sorter.event_handeler()


main()