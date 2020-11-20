import pygame

# Variables
screen_width = 800
screen_height = 500
screen_size = (screen_width, screen_height)
white = (255, 255, 255)
black = (0, 0, 0)

# Paddles
paddle_width = 20
paddle_height = 150


paddle_1_x = 10
paddle_1_y = (screen_height // 2) - (paddle_height // 2)
paddle_1_y_change = 0

paddle_2_x = screen_width - 10 - paddle_width
paddle_2_y = (screen_height // 2) - (paddle_height // 2)
paddle_2_y_change = 0

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pong')

# Net
net_width = 2
net_height = 20
net_x = (screen_width // 2) - (net_width // 2)
net_y = 0

# Ball
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_radius = 10
ball_x_change = 1
ball_y_change = 1
# Score
player_1_score = 0
player_1_score_x = screen_width // 4
player_1_score_y = 5

player_2_score = 0
player_2_score_x = screen_width - (screen_width // 4)
player_2_score_y = 5


clock = pygame.time.Clock()
fps = 200

myfont = pygame.font.SysFont("monospace", 65)


def draw_paddle(x, y, width, height):
    pygame.draw.rect(screen, white, (x, y, width, height))


def draw_net(x, y, width, height):
    for i in range(y, 500, 30):
        pygame.draw.rect(screen, white, (x, y + i, width, height))


def draw_ball(x, y, radius):
    pygame.draw.circle(screen, white, (x, y), radius)


def check_collision_paddle_1():
    ball_top = ball_y - ball_radius
    ball_bottom = ball_y + ball_radius
    ball_left = ball_x - ball_radius
    ball_right = ball_x + ball_radius

    paddle_top = paddle_1_y
    paddle_bottom = paddle_1_y + paddle_height
    paddle_left = paddle_1_x
    paddle_right = paddle_1_x + paddle_width

    return ball_top < paddle_bottom and ball_bottom > paddle_top and ball_left < paddle_right and ball_right > paddle_left


def check_collision_paddle_2():
    ball_top = ball_y - ball_radius
    ball_bottom = ball_y + ball_radius
    ball_left = ball_x - ball_radius
    ball_right = ball_x + ball_radius

    paddle_top = paddle_2_y
    paddle_bottom = paddle_2_y + paddle_height
    paddle_left = paddle_2_x
    paddle_right = paddle_2_x + paddle_width

    return ball_top < paddle_bottom and ball_bottom > paddle_top and ball_left < paddle_right and ball_right > paddle_left


def reset_ball():
    global ball_x_change, ball_y_change
    ball_x = screen_width // 2
    ball_y = screen_height // 2
    ball_radius = 10
    ball_x_change = -ball_x_change
    ball_y_change = -ball_y_change


def check_score():
    global player_1_score, player_2_score
    if ball_x <= 0:
        player_2_score += 1
        reset_ball()
    if ball_x >= screen_width:
        player_1_score += 1
        reset_ball()


def print_score(score, x, y):
    score_text = myfont.render(str(score), True, white)
    screen.blit(score_text, (x, y))


running = True

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_2_y_change = -5
            if event.key == pygame.K_DOWN:
                paddle_2_y_change = 5
            if event.key == pygame.K_w:
                paddle_1_y_change = -5
            if event.key == pygame.K_s:
                paddle_1_y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle_2_y_change = 0
            if event.key == pygame.K_DOWN:
                paddle_2_y_change = 0
            if event.key == pygame.K_w:
                paddle_1_y_change = 0
            if event.key == pygame.K_s:
                paddle_1_y_change = 0

    pygame.draw.rect(screen, black, (0, 0, screen_width, screen_height))

    # Moving the ball
    ball_x += ball_x_change
    ball_y += ball_y_change

    paddle_1_y += paddle_1_y_change
    paddle_2_y += paddle_2_y_change

    if ball_y >= screen_height or ball_y <= 0:
        ball_y_change = -ball_y_change

    if paddle_1_y + paddle_height >= screen_height or paddle_1_y <= 0:
        paddle_1_y_change = 0

    if paddle_2_y + paddle_height >= screen_height or paddle_2_y <= 0:
        paddle_2_y_change = 0

    paddle_1_collision = check_collision_paddle_1()
    paddle_2_collision = check_collision_paddle_2()

    if paddle_1_collision or paddle_2_collision:
        ball_x_change = -ball_x_change
        ball_y_change = -ball_y_change

    draw_paddle(paddle_1_x, paddle_1_y, paddle_width, paddle_height)
    draw_paddle(paddle_2_x, paddle_2_y, paddle_width, paddle_height)
    draw_net(net_x, net_y, net_width, net_height)
    draw_ball(ball_x, ball_y, ball_radius)

    check_score()
    print_score(player_1_score, player_1_score_x, player_1_score_y)
    print_score(player_2_score, player_2_score_x, player_2_score_y)

    pygame.display.update()

pygame.quit()
