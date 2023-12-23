import pygame
import random

# Начать игру
pygame.init()

# Цветы игры
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Размер и название поля
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Характеристики поля (Функция)
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 20
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self):
        self.size = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = -3

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size)

class Brick:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.x = x
        self.y = y
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# Crear objetos
paddle = Paddle()
ball = Ball()
bricks = []
for i in range(8):
    for j in range(6):
        brick = Brick(90 + i * 100, 50 + j * 30)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение доски кнопками направо и налево
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle.speed
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle.speed

    # Ограничение доски внутпри
    if paddle.x < 0:
        paddle.x = 0
    if paddle.x > WIDTH - paddle.width:
        paddle.x = WIDTH - paddle.width

    # Движение шара
    ball.x += ball.speed_x
    ball.y += ball.speed_y

    # Удар с шаром
    if ball.y + ball.size >= paddle.y and ball.x + ball.size >= paddle.x and ball.x - ball.size <= paddle.x + paddle.width:
        ball.speed_y *= -1

    # Удар с кирпичами
    for brick in bricks:
        if brick.visible and ball.y - ball.size <= brick.y + brick.height and ball.x + ball.size >= brick.x and ball.x - ball.size <= brick.x + brick.width:
            brick.visible = False
            ball.speed_y *= -1

    # Удар с границами 
    if ball.x - ball.size <= 0 or ball.x + ball.size >= WIDTH:
        ball.speed_x *= -1
    if ball.y - ball.size <= 0:
        ball.speed_y *= -1

    # Окончание игры при контакте шара с ограничением
    
    if ball.y - ball.size > HEIGHT:
        running = False

    # Рисовать элементы
    screen.fill(BLACK)
    paddle.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()

    # Чтобы показать все изменения на поле
    pygame.display.flip()

    # Время игры
    clock.tick(60)

# Выходить из игры
pygame.quit()
