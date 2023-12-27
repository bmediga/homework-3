from braulio import Paddle, Ball, Brick

def test_paddle_initialization():
    paddle = Paddle()
    assert paddle.width == 100
    assert paddle.height == 10
    assert paddle.x == 350
    assert paddle.y == 580
    assert paddle.speed == 5

def test_ball_initialization():
    ball = Ball()
    assert ball.size == 10
    assert ball.x == 400
    assert ball.y == 300
    assert ball.speed_x in [-3, 3]
    assert ball.speed_y == -3

def test_brick_initialization():
    brick = Brick(100, 50)
    assert brick.width == 60
    assert brick.height == 20
    assert brick.x == 100
    assert brick.y == 50
    assert brick.visible

def test_brick_collision():
    brick = Brick(100, 50)
    ball = Ball()
    ball.x = 100
    ball.y = 50
    assert brick.collision(ball) == True

def test_paddle_collision():
    paddle = Paddle()
    ball = Ball()
    ball.x = paddle.x
    ball.y = paddle.y
    assert paddle.collision(ball) == True

# Otras pruebas que desees añadir...
