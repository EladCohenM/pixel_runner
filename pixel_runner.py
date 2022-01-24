from msilib.schema import Font
import random
from re import T
from tkinter import CENTER
import pygame
from sys import exit
#self define modules
from player import Player
from obstacle import Obstacle

# game initialization
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()

#global variables
start_time = 0
game_active = False
bg_music = pygame.mixer.Sound("./audio/music.wav")
bg_music.set_volume(0.5)
bg_music.play(loops=-1)
with open("./best score.txt","r") as file:
    best_score = int(file.read())

print(best_score)

# colors
grey = (64, 64, 64)
blue = (94, 129, 162)
turqoise = (111, 196, 169)

# font
font = pygame.font.Font("./font/Pixeltype.ttf", 50)


def create_font(fstr, color, coordinates):
    font_surf = font.render(fstr, False, color)
    font_rect = font_surf.get_rect(center=coordinates)
    screen.blit(font_surf, font_rect)


# images
ground = pygame.image.load("./graphics/ground.png").convert()
sky = pygame.image.load("./graphics/sky.png").convert()
player_stand = pygame.transform.rotozoom(pygame.image.load(
    "./graphics/Player/player_stand.png").convert_alpha(), 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Player sprite Class
player = pygame.sprite.GroupSingle()
player.add(Player())

# Obstacles Class
obstacles = pygame.sprite.Group()
create_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(create_enemy_event, 1200)

# game logic
def collision():
    global best_score
    if pygame.sprite.spritecollide(player.sprite, obstacles, True):
        obstacles.empty()
        score_sec = (current_time - start_time)//1000
        if score_sec > best_score:
            best_score = score_sec
        return False
    else:
        return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("./best score.txt", "w") as file:
                file.write(str(best_score))
            pygame.quit()
            exit()

        if game_active:
            if event.type == create_enemy_event:
                obstacles.add(Obstacle(random.choice(
                    ["snail", "snail", "snail", "fly"])))

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()

    if game_active:
        player.update()
        obstacles.update()
        game_active = collision()

        current_time = pygame.time.get_ticks()
        score = f"{(current_time - start_time)//1000//60}:{(current_time - start_time)//1000%60}"

        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        create_font(f"Score     {score}", grey, (400, 50))
        obstacles.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(60)

    else:
        screen.fill(blue)
        create_font(f"Pixel Runner", turqoise, (400, 80))
        if start_time:
            create_font(f"Last Score    {score}", turqoise, (400, 330))
            create_font(f"Best Score    {best_score//60}:{best_score%60}", turqoise, (400, 370))
        else:
            create_font(f"Press space to start", turqoise, (400, 330))
            create_font(f"Best Score   {best_score//60}:{best_score%60}", turqoise, (400, 370))
        screen.blit(player_stand, player_stand_rect)
        pygame.display.update()
        clock.tick(60)
