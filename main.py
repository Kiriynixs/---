from os import path
from tkinter import*
import pygame
import random
import menu
from gameOver4 import pic4
# from PIL import ImageTk, Image
from phone1 import pic1

# игровые переменные
WIDTH = 750
HEIGHT = 750

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# создание игрового окна из шаблона
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
clock = pygame.time.Clock()

# mainmenu = menu.Menu(screen)
#
# mainmenu.add.button("Играть", mainmenu.disable)
# mainmenu.add.button("Выход", quit)

img_dir= path.join(path.dirname(__file__), "IMG")
music_dir= path.join(path.dirname(__file__), "music")
bg = pygame.image.load(path.join(img_dir, "Фон_крестики_нолики.jpg")).convert()
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
bg_rect= bg.get_rect()
pygame.mixer.music.load(path.join(music_dir,"music_No_Roots_.mp3"))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
win_sound=pygame.mixer.Sound(path.join(music_dir,"game-won.mp3"))
win_sound.set_volume(0.5)
lost_sound=pygame.mixer.Sound(path.join(music_dir,"ty-proigral-game-lost.mp3"))
lost_sound.set_volume(0.5)

# список значений в клетках построчно
field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
# переменная цикла
run = True
# переменная проверки завершения игры
game_over = False


# отрисовка сетки
def draw_grid():
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 750), 3)
    pygame.draw.line(screen, (0, 0, 0), (500, 0), (500, 750), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (750, 250), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 500), (750, 500), 3)


def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "0":
                pygame.draw.circle(screen, BLACK, (j * 250 + 125, i * 250 + 125), 125, 3)

            elif field[i][j] == "x":
                pygame.draw.line(screen, (0, 0, 0), (j * 250 + 5, i * 250 + 5), (j * 250 + 245, i * 250 + 245), 3)
                pygame.draw.line(screen, (0, 0, 0), (j * 250 + 245, i * 250 + 5), (j * 250 + 5, i * 250 + 245), 3)


# вычисление результата игры
def get_win_check(symbol):  # передаём список и символ участника
    flag_win = False
    global win
    # перебираем подсписки
    for line in field:
        if line.count(symbol) == 3:  # если в подсписке все 3 символа совпадают=горизонтальный ряд
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
    # собрана вертикальный ряд
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            flag_win = True
            win = [[i, 0], [i, 1], [i, 2]]
            print(win)
    # проверка на диагональные линии
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
        print(win)
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
        print(win)
    return flag_win


while run:
    clock.tick(FPS)  # переключение кадров
    # цикл проверки всех событий
    events = pygame.event.get()
    # for event in events:
    for event in events:
        if event.type == pygame.QUIT:  # проверка нажатия на "закрыть"
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # проверка клика мышки на поле
            pos = pygame.mouse.get_pos()  # сюдаааааа координаты мышки

            if field[pos[1] // 250][pos[0] // 250] == "":  # на какое поле нажали
                field[pos[1] // 250][pos[0] // 250] = "x"  # присваивание значения нажатия(всегда играем за крестик)
                x, y = random.randint(0, 2), random.randint(0, 2)  # первая генерация клетки
                while field[x][y] != "":  # пока эта клетка не пуста
                    x, y = random.randint(0, 2), random.randint(0, 2)  # генерируем другую
                field[x][y] = "0"

            player_win = get_win_check("x")  # проверка на выигрыш игрока
            ai_win = get_win_check("0")  # проверка на выигрыш бота
            rezult = field[0].count("x") + field[0].count("0") + field[1].count("x") + field[1].count("0") + field[
                2].count("x") + field[2].count("0")
            if player_win or ai_win:  # проверяем выиграл ли кто-нибудь
                game_over = True  # останавливаем проверку кликов мышкой
                if player_win:
                    pygame.display.set_caption("Вы победили")
                    win_sound.play()
                    pygame.draw.rect(screen, GREEN, (win[0][0] * 250, win[0][1] * 250, 250, 250))
                    pygame.draw.rect(screen, GREEN, (win[1][0] * 250, win[1][1] * 250, 250, 250))
                    pygame.draw.rect(screen, GREEN, (win[2][0] * 250, win[2][1] * 250, 250, 250))
                    pygame.display.flip()
                    pic1()
                else:
                    pygame.display.set_caption("Компьютер победил")
                    lost_sound.play()
                    pic4()
            # cкладываем количество крестов и нулей в каждой строке списка(4 хода игрок+4 хода бот = 8)
            elif rezult == 8:
                pygame.display.set_caption("Ничья")
    # отрисовка всех элементов
    screen.blit(bg,bg_rect)
    # if game_over:
        # pygame.draw.rect(screen, GREEN, (win[0][0] * 250, win[0][1] * 250, 250, 250))
        # pygame.draw.rect(screen, GREEN, (win[1][0] * 250, win[1][1] * 250, 250, 250))
        # pygame.draw.rect(screen, GREEN, (win[2][0] * 250, win[2][1] * 250, 250, 250))
    draw_tic_tac_toe()
    draw_grid()
    # mainmenu.flip(events)
    pygame.display.flip()
pygame.quit()
print("Привет, Жанара")
print()


