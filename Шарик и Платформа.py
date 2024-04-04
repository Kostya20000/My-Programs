import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры игрового окна
win_width = 1500
win_height = 750
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Шарик и Платформа")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Параметры мяча
ball_radius = 10
ball_x = win_width // 2
ball_y = win_height // 2
ball_speed_x = 1
ball_speed_y = 1

# Параметры платформы
platform_width = 100
platform_height = 10
platform_x = win_width // 2 - platform_width // 2
platform_y = win_height - 50
platform_speed = 2

# Флаг проигрыша
game_over = False

# Переменная для хранения очков
очки = 0

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    if not game_over:
        # Обновление координат мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Отскок от стен
        if ball_x <= 0 or ball_x >= win_width:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:
            ball_speed_y = -ball_speed_y

        # Отскок от платформы
        if ball_y + ball_radius >= platform_y and platform_x <= ball_x <= platform_x + platform_width and ball_speed_y > 0:
            ball_speed_y = -ball_speed_y
            очки += 1  # Начисление 10 очков при отскоке от платформы
            ball_speed_x *= 1.1  # Увеличение скорости шарика на 10%
            ball_speed_y *= 1.1  # Увеличение скорости шарика на 10%
            platform_speed *= 1.1  # Увеличение скорости шарика на 10%
        # Проверка на проигрыш
        if ball_y > win_height:
            game_over = True

        # Управление платформой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and platform_x > 0:
            platform_x -= platform_speed
        if keys[pygame.K_RIGHT] and platform_x < win_width - platform_width:
            platform_x += platform_speed

    # Отображение элементов
    win.fill(black)
    pygame.draw.circle(win, blue, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(win, white, (platform_x, platform_y, platform_width, platform_height))

    # Отображение количества очков на экране
    font = pygame.font.Font(None, 36)
    text = font.render("Очки: " + str(очки), True, white)
    win.blit(text, (10, 10))

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over :(", True, white)
        win.blit(text, (win_width//2 - 70, win_height//2))

    pygame.display.update()
