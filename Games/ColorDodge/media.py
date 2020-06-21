import pygame

pygame.init()


# ----------------------------------------------------------
# IMAGE LOADING
# ----------------------------------------------------------
def rocket_image() -> object:
    rocket: object = pygame.image.load("images/Rocket.png")
    rocket = pygame.transform.scale(rocket, (200, 200))
    return rocket


def explosion_image():
    explosion: object = pygame.image.load("images/Explosion.png")
    explosion = pygame.transform.scale(explosion, (200, 200))
    return explosion


def asteroid_red():
    asteroid: object = pygame.image.load("images/Asteroid_Red.png")
    asteroid = pygame.transform.scale(asteroid, (150, 150))
    return asteroid


def asteroid_blue():
    asteroid: object = pygame.image.load("images/Asteroid_Blue.png")
    asteroid = pygame.transform.scale(asteroid, (150, 150))
    return asteroid


def asteroid_yellow():
    asteroid: object = pygame.image.load("images/Asteroid_Yellow.png")
    asteroid = pygame.transform.scale(asteroid, (150, 150))
    return asteroid


def asteroid_green():
    asteroid: object = pygame.image.load("images/Asteroid_Green.png")
    asteroid = pygame.transform.scale(asteroid, (150, 150))
    return asteroid


def asteroid_purple():
    asteroid: object = pygame.image.load("images/Asteroid_Purple.png")
    asteroid = pygame.transform.scale(asteroid, (150, 150))
    return asteroid


# ----------------------------------------------------------
# SOUND LOADING
# ----------------------------------------------------------

def click_sound():
    click = pygame.mixer.Sound("sounds/click.wav")
    return click


def explode_sound():
    explode = pygame.mixer.Sound("Sounds/Explode.wav")
    return explode


def lose_sound():
    lose = pygame.mixer.Sound("Sounds/Lose Sound.wav")
    return lose


def point_sound():
    point = pygame.mixer.Sound("Sounds/Point Score Sound.wav")
    return point


def music_load():
    music = pygame.mixer.music.load("Sounds/Game Music.wav")
    return music


# ----------------------------------------------------------
# FONTS
# ----------------------------------------------------------
def pixel_font(size):
    this_font: object = pygame.font.Font("Fonts/Video Game Font.ttf", size)
    return this_font


# ----------------------------------------------------------
# SPRITE HANDLE
# ----------------------------------------------------------
def asteroid_sprite(color: object) -> object:
    if color == 0:
        return asteroid_red()
    elif color == 1:
        return asteroid_blue()
    elif color == 2:
        return asteroid_green()
    elif color == 3:
        return asteroid_yellow()
    elif color == 4:
        return asteroid_purple()


def rocket_sprite():
    return rocket_image()
