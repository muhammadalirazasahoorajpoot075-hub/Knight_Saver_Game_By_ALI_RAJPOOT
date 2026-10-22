#Knight_Saving_ Game_By_ALI_RAJPOOT.
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KNIGHT SAVER - ALI RAJPOOT")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (220, 50, 50)
GREEN = (46, 204, 113)
GOLD = (255, 215, 0)
BLUE = (52, 152, 219)
GRAY = (100, 100, 100)
BG = (30, 30, 60)
BLACK = (10, 10, 20)

font = pygame.font.Font(None, 28)
big_font = pygame.font.Font(None, 48)

player = pygame.Rect(385, 285, 30, 30)
speed = 5
health = 100
score = 0
level = 1
hit_cd = 0
game_over = False

def new_enemy():
    return {
        "rect": pygame.Rect(
            random.randint(0, WIDTH - 25),
            random.randint(40, HEIGHT - 60),
            25, 25
        ),
        "dx": random.choice([-2, 2]),
        "dy": random.choice([-2, 2])
    }

def new_save():
    while True:
        r = pygame.Rect(
            random.randint(40, WIDTH - 40),
            random.randint(50, HEIGHT - 50),
            20, 20
        )
        if not r.colliderect(player.inflate(120, 120)):
            return r

enemies = [new_enemy() for _ in range(5)]
saves = [new_save() for _ in range(5)]

# Touch control buttons
buttons = {
    "UP": pygame.Rect(90, 430, 60, 50),
    "DOWN": pygame.Rect(90, 530, 60, 50),
    "LEFT": pygame.Rect(25, 480, 60, 50),
    "RIGHT": pygame.Rect(155, 480, 60, 50)
}

def draw_button(rect, label):
    pygame.draw.rect(screen, BLUE, rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=10)
    txt = font.render(label, True, WHITE)
    screen.blit(
        txt,
        (rect.centerx - txt.get_width() // 2,
         rect.centery - txt.get_height() // 2)
    )

running = True

while running:
    clock.tick(60)
    move_x = 0
    move_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.topleft = (385, 285)
                health = 100
                score = 0
                level = 1
                hit_cd = 0
                enemies = [new_enemy() for _ in range(5)]
                saves = [new_save() for _ in range(5)]
                game_over = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if restart_button.collidepoint(event.pos):
                    player.topleft = (385, 285)
                    health = 100
                    score = 0
                    level = 1
                    hit_cd = 0
                    enemies = [new_enemy() for _ in range(5)]
                    saves = [new_save() for _ in range(5)]
                    game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move_x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move_x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            move_y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            move_y += speed

        # Mouse and touchscreen buttons
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            pos = pygame.mouse.get_pos()
            for name, rect in buttons.items():
                if rect.collidepoint(pos):
                    if name == "UP":
                        move_y -= speed
                    elif name == "DOWN":
                        move_y += speed
                    elif name == "LEFT":
                        move_x -= speed
                    elif name == "RIGHT":
                        move_x += speed

        player.x += move_x
        player.y += move_y

        player.clamp_ip(pygame.Rect(0, 20, WIDTH, HEIGHT - 40))

        if hit_cd > 0:
            hit_cd -= 1

    screen.fill(BG)
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 20))
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 20, WIDTH, 20))

    if not game_over:
        for enemy in enemies:
            enemy["rect"].x += enemy["dx"]
            enemy["rect"].y += enemy["dy"]

            if enemy["rect"].left <= 0 or enemy["rect"].right >= WIDTH:
                enemy["dx"] *= -1

            if enemy["rect"].top <= 20 or enemy["rect"].bottom >= HEIGHT - 20:
                enemy["dy"] *= -1

            pygame.draw.rect(screen, RED, enemy["rect"])

            if hit_cd == 0 and player.colliderect(enemy["rect"]):
                health -= 10
                hit_cd = 30
                enemy["rect"].topleft = (
                    random.randint(0, WIDTH - 30),
                    random.randint(30, HEIGHT - 50)
                )

                if health <= 0:
                    health = 0
                    game_over = True

        for saved in saves[:]:
            pygame.draw.rect(screen, GREEN, saved)
            pygame.draw.rect(
                screen, GOLD,
                (saved.x + 2, saved.y - 6, 16, 5)
            )

            if player.colliderect(saved):
                saves.remove(saved)
                score += 1
                saves.append(new_save())

                if score % 5 == 0:
                    level += 1
                    enemies.append(new_enemy())

        info = font.render(
            f"LEVEL: {level}  SAVED: {score}  HP: {health}%",
            True, WHITE
        )
        screen.blit(info, (15, 25))

        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(
            screen, GOLD,
            (player.x + 5, player.y - 7, 20, 7)
        )

        for name, rect in buttons.items():
            draw_button(rect, name)

    else:
        title = big_font.render("GAME OVER", True, GOLD)
        result = font.render(
            f"Saved: {score}   Level: {level}",
            True, WHITE
        )
        restart_text = font.render("PLAY AGAIN", True, WHITE)

        screen.blit(
            title,
            (WIDTH // 2 - title.get_width() // 2, 200)
        )
        screen.blit(
            result,
            (WIDTH // 2 - result.get_width() // 2, 260)
        )

        restart_button = pygame.Rect(
            WIDTH // 2 - 90, 320, 180, 55
        )
        pygame.draw.rect(
            screen, GREEN, restart_button, border_radius=10
        )
        screen.blit(
            restart_text,
            (restart_button.centerx - restart_text.get_width() // 2,
             restart_button.centery - restart_text.get_height() // 2)
        )

    pygame.display.flip()

pygame.quit()
sys.exit()
