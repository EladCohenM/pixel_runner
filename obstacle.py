import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.img_index = 0
        if type == "fly":
            fly1 = pygame.image.load("./graphics/Fly/Fly1.png")
            fly2 = pygame.image.load("./graphics/Fly/Fly2.png")
            self.img_list = [fly1, fly2]
            self.image = self.img_list[self.img_index]
            self.rect = self.image.get_rect(
                midbottom=(random.randint(900, 1200), 210))
        else:
            snail1 = pygame.image.load("./graphics/snail/snail1.png")
            snail2 = pygame.image.load("./graphics/snail/snail2.png")
            self.img_list = [snail1, snail2]
            self.image = self.img_list[self.img_index]
            self.rect = self.image.get_rect(
                midbottom=(random.randint(900, 1100), 300))

    def animation(self):
        self.image = self.img_list[int(self.img_index)]
        if self.type == "fly":
            self.img_index += 0.49
        else:
            self.img_index += 0.1
        if self.img_index >= 2:
            self.img_index = 0

    def update(self):
        self.animation()
        self.rect.x += -6
        if self.rect.x <= -100:
            self.kill()
