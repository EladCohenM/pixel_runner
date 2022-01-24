import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load("./graphics/Player/player_walk_1.png")
        player_walk2 = pygame.image.load("./graphics/Player/player_walk_2.png")
        self.jump = pygame.image.load("./graphics/Player/jump.png")
        self.img_list = [player_walk1, player_walk2]
        self.player_img_index = 0
        self.image = self.img_list[self.player_img_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("./audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        self.player_img_index += 0.1
        if self.player_img_index >= 2:
            self.player_img_index = 0
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.image = self.img_list[int(self.player_img_index)]

    def update(self):
        self.movement()
        self.animation()

