import pygame
import time
import random

pygame.init()

# Определение цветов
белый = (255, 255, 255)
черный = (0, 0, 0)
красный = (213, 50, 80)
зеленый = (0, 255, 0)
синий = (50, 153, 213)

# Определение размеров окна и других параметров
размер_блока = 10
окно_ширина = 800
окно_высота = 600

# Настройка окна
окно = pygame.display.set_mode((окно_ширина, окно_высота))
pygame.display.set_caption('Змейка')

# Функция отрисовки змейки на игровом поле
def рисовать_змейку(размер_блока, змейка_список):
    for x in змейка_список:
        pygame.draw.rect(окно, зеленый, [x[0], x[1], размер_блока, размер_блока])

# Основной игровой цикл
def игра():
    игра_завершена = False
    игровая_скорость = 15

    x = окно_ширина / 2
    y = окно_высота / 2

    x_изм = 0
    y_изм = 0

    змейка_список = []
    длина_змейки = 1

    еда_x = round(random.randrange(0, окно_ширина - размер_блока) / 10.0) * 10.0
    еда_y = round(random.randrange(0, окно_высота - размер_блока) / 10.0) * 10.0

    while not игра_завершена:
        while игра_завершена == True:
            окно.fill(черный)
            шрифт = pygame.font.SysFont(None, 55)
            текст = шрифт.render("Игра завершена. Нажмите C для продолжения или Q для выхода.", True, красный)
            окно.blit(текст, (окно_ширина / 6, окно_высота / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        игра_завершена = True
                        игра_активна = False
                    if event.key == pygame.K_c:
                        игра()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                игра_завершена = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_изм = -размер_блока
                    y_изм = 0
                elif event.key == pygame.K_RIGHT:
                    x_изм = размер_блока
                    y_изм = 0
                elif event.key == pygame.K_UP:
                    y_изм = -размер_блока
                    x_изм = 0
                elif event.key == pygame.K_DOWN:
                    y_изм = размер_блока
                    x_изм = 0

        if x >= окно_ширина or x < 0 or y >= окно_высота or y < 0:
            игра_завершена = True

        x += x_изм
        y += y_изм
        окно.fill(черный)
        pygame.draw.rect(окно, красный, [еда_x, еда_y, размер_блока, размер_блока])
        змей_голова = []
        змей_голова.append(x)
        змей_голова.append(y)
        змейка_список.append(змей_голова)
        if len(змейка_список) > длина_змейки:
            del змейка_список[0]

        for каждый in змейка_список[:-1]:
            if каждый == змей_голова:
                игра_завершена = True

        рисовать_змейку(размер_блока, змейка_список)

        pygame.display.update()

        if x == еда_x and y == еда_y:
            еда_x = round(random.randrange(0, окно_ширина - размер_блока) / 10.0) * 10.0
            еда_y = round(random.randrange(0, окно_высота - размер_блока) / 10.0) * 10.0
            длина_змейки += 1

        время = pygame.time.Clock()
        время.tick(игровая_скорость)



игра()