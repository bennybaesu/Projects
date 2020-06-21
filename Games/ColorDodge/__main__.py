import pygame
import random
import time
import media
import asteroid
import rocket

# ----------------------------------------------------------
# INITIALIZING VALUES
# ----------------------------------------------------------
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()  # Initialize Pygame

# Display Settings:
window_width = 1200
window_height = 750
display_size = (window_width, window_height)
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Color Dodge')
clock = pygame.time.Clock()
x_change = 0
car_width = 200
change_speed = 7
score = 0
goal = 3
goal_current = 0
initial_ast = 200
current_color = random.randrange(0, 5)  # Initial safe color
update_when = random.randrange(2, 6)  # Picks when the safe color updates
exploded = False
game_start = True
sound_on = True
music_on = True
highscore = 0

with open('highscore.txt', 'r') as highscoreFile:
    highscore = highscoreFile.read()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)

# Asteroids
ast_list = [asteroid.Asteroid(200, window_width), asteroid.Asteroid(550, window_width),
            asteroid.Asteroid(900, window_width), asteroid.Asteroid(1250, window_width),
            asteroid.Asteroid(1600, window_width)]

# Rocket
rocket_ = rocket.Rocket(window_width * 0.44, window_height * 0.7, car_width, car_width)

music = media.music_load()
pygame.mixer.music.set_volume(.4)
pygame.mixer.music.play(-1)


# ----------------------------------------------------------

def rocket(exploded):
    screen.blit(rocket_.sprite, (rocket_.x, rocket_.y))
    if exploded:
        explosion()


def asteroid():
    for ast in ast_list:
        screen.blit(ast.sprite, (ast.x, ast.y))


def explosion():
    screen.blit(rocket_.explosion_sprite, (rocket_.x, rocket_.y))


def asteroid_hitbox_update():
    for ast in ast_list:
        ast.update()


def fall(s):
    ast_list[0].fall(s)
    ast_list[1].fall(s)
    ast_list[2].fall(s)
    ast_list[3].fall(s)
    ast_list[4].fall(s)


def display_score(s):
    button_score = "Score: " + str(s)
    score_txt = media.pixel_font(50).render(button_score, True, white)
    screen.blit(score_txt, (5, 5))


def display_current_color(c):
    current_msg = "Safe Color:"
    current_txt = media.pixel_font(30).render(current_msg, True, white)
    screen.blit(current_txt, (650, 10))
    t = ' '
    cc = (0, 0, 0)
    if c == 0:
        t = 'RED'
        cc = red
    elif c == 1:
        t = 'BLUE'
        cc = blue
    elif c == 2:
        t = 'GREEN'
        cc = green
    elif c == 3:
        t = 'YELLOW'
        cc = yellow
    elif c == 4:
        t = 'PURPLE'
        cc = purple
    color_txt = media.pixel_font(30).render(t, True, cc)
    screen.blit(color_txt, (1000, 10))


def collided(x_car, y_car, cc):
    for ast in ast_list:
        if not ast.hit:
            if ast.center[1] - ast.radius < rocket_.hitbox[1] + rocket_.hitbox[3] and ast.center[1] + ast.radius > \
                    rocket_.hitbox[1]:
                if ast.center[0] - ast.radius < rocket_.hitbox[0] + rocket_.hitbox[2] and ast.center[0] + ast.radius > \
                        rocket_.hitbox[0]:
                    ast.hit = True
                    if ast.color == cc:
                        return True, False
                    else:
                        return False, True

    return False, False  # It didn't collide, but we don't add anything to the score


def new_update_timeline():
    u = random.randrange(2, 6)
    return u


def update_safe(c):
    cc = 0
    while True:
        cc = random.randrange(0, 5)
        if cc != c:
            break

    return cc


def highscoreSet(currentScore):
    with open('highscore.txt', 'r') as highscoreFileRead:
        h = int(highscoreFileRead.read())

    if currentScore <= h:
        return False, h
    else:
        with open('highscore.txt', 'w') as highscoreFileWrite:
            highscoreFileWrite.write(str(currentScore))
            return True, currentScore


def game_over(s, n, h):
    gg = True
    while gg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gg = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gg = False

        screen.fill(black)
        asteroid()
        rocket(False)
        explosion()
        display_score(s)
        display_highscore(n, h)
        game_over_msg = "GAME OVER"
        game_over_txt = media.pixel_font(100).render(game_over_msg, True, white)
        screen.blit(game_over_txt, (window_width / 8 - 10, window_height / 2 - 20))
        cont = "Click anywhere to continue"
        cont_txt = media.pixel_font(18).render(cont, True, white)
        screen.blit(cont_txt, (window_width / 3 - 40, window_height / 2 + 75))

        pygame.display.update()


def display_highscore(n, h):
    if n:
        new_message = "NEW HIGH SCORE!"
        new_txt = media.pixel_font(30).render(new_message, True, white)
        screen.blit(new_txt, (window_width / 2 - 245, window_height / 3 - 90))
    highscore_msg = "Highscore " + str(h)
    highscore_txt = media.pixel_font(40).render(highscore_msg, True, white)
    screen.blit(highscore_txt, (window_width / 3 - 40, window_height / 2 - 100))


def main_menu(s, m):
    m_on = m
    s_on = s
    if m_on:
        pygame.mixer.music.unpause()
    button_music = pygame.Rect(180, 9, 28, 28)
    button_sound = pygame.Rect(180, 50, 28, 28)
    mm = True
    while mm:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                mm = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_music.collidepoint(mx, my):
                    if m_on:
                        m_on = False
                        if s_on:
                            media.click_sound().play()
                        pygame.mixer.music.pause()
                    else:
                        m_on = True
                        if s_on:
                            media.click_sound().play()
                        pygame.mixer.music.unpause()
                elif button_sound.collidepoint(mx, my):
                    if s_on:
                        s_on = False
                    else:
                        s_on = True
                        media.click_sound().play()
                else:
                    if s_on:
                        media.click_sound().play()
                    return False, s_on, m_on

        screen.fill(black)
        title = "COLOR DODGE"
        music_title = "Music Off:"
        sounds_title = "Sounds Off:"
        play_title = "Click anywhere to play!"
        title_txt = media.pixel_font(100).render(title, True, white)
        music_txt = media.pixel_font(15).render(music_title, True, white)
        sounds_txt = media.pixel_font(15).render(sounds_title, True, white)
        play_txt = media.pixel_font(18).render(play_title, True, white)
        screen.blit(title_txt, (window_width / 20 - 10, window_height / 2 - 100))
        screen.blit(music_txt, (7, 20))
        screen.blit(sounds_txt, (5, 55))
        screen.blit(play_txt, (window_width / 3 - 40, window_height / 2 + 30))

        if m_on:
            pygame.draw.rect(screen, white, button_music, 2)
        else:
            pygame.draw.rect(screen, white, button_music)

        if s_on:
            pygame.draw.rect(screen, white, button_sound, 2)
        else:
            pygame.draw.rect(screen, white, button_sound)

        rocket(False)
        pygame.display.update()
    return False


# ----------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------
running = True
collision = False
iterator = False
newHigh = False

while running:
    # If some kind of change is detected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if the user exits out
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # If the user presses the left key
                x_change = -change_speed
            elif event.key == pygame.K_RIGHT:  # If the user presses the right key
                x_change = change_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0  # No change if the user presses the up or down keys

    # Change the position based on where the user moved:
    rocket_.x += x_change
    if rocket_.x > (window_width - car_width):  # Don't let the user move all the way to the right
        rocket_.x = window_width - car_width  # Don't let the user move all the way to the left
    if rocket_.x < 0:
        rocket_.x = 0

    rocket_.update()

    screen.fill(black)  # Set the background

    if game_start:
        game_start, sound_on, music_on = main_menu(sound_on, music_on)

    asteroid()  # Display the asteroids
    display_score(score)  # Display the score

    if not exploded:
        display_current_color(current_color)  # Display the safe color

    fall(change_speed)  # Make the asteroids fall
    asteroid_hitbox_update()
    rocket(exploded)  # Display the rocket at its current position

    iterator, collision = collided(rocket_.x, rocket_.y, current_color)
    if collision:
        exploded = True
        pygame.mixer.music.pause()
        if sound_on:
            media.explode_sound().play()
        change_speed = 0
        game_round = 0
        if sound_on:
            media.lose_sound().play()
        newHigh, highscore = highscoreSet(score)
        game_over(score, newHigh, highscore)
        current_color = random.randrange(0, 5)
        for ast in ast_list:
            ast.new_game(initial_ast, window_width)
            initial_ast += 350

        rocket_.reset(window_width * 0.44, window_height * 0.7)
        score = 0
        goal = 3
        goal_current = 0
        change_speed = 7
        x_change = 0
        exploded = False
        game_start = True
        iterator = False
        collision = False
        initial_ast = 200

    if iterator:
        score = score + 1
        if sound_on:
            media.point_sound().play()
        goal_current += 1
        update_when -= 1
        pygame.display.update()

    if goal_current == goal:
        goal += 1
        change_speed += 1
        goal_current = 0

    if update_when == 0:
        current_color = update_safe(current_color)
        update_when = new_update_timeline()

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit game
pygame.quit()
quit()
