from turtle import Screen
from ship import Ship
from enemy import Enemy
from bullet import Bullet
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

ship = Ship((0, -250))

bullet = Bullet()

enemy = Enemy((700, 100))


blocks = []
x1 = 0
for i in range(5):
    x = -480
    x1 += 160
    i = Enemy((x + x1, 250))
    q = Enemy((x + x1, 150))
    blocks.append(i)
    blocks.append(q)

def bombs():
    print("BOMO")
    if running == True and elapsed_time % 5 == 0 and elapsed_time % 10 != 0:
        for n, i in enumerate(blocks):
            if i.ycor() < 200:
                i.go_right()
            else:
                i.go_left()
def bombs2():
    print("BOMO2")
    print(elapsed_time)
    if running == True and elapsed_time % 10 == 0:
        print('BINGO')
        for n, i in enumerate(blocks):
            if i.ycor() > 200:
                i.go_right()
            else:
                i.go_left()
flag = True
def bombers():
    global flag

    bullet.bully.goto(200, 200)

    bullet.bully.forward(2)

screen.onkey(ship.go_left, "a")
screen.onkey(ship.go_right, "d")
screen.onkey(bullet.shoot, "w")
screen.listen()

game_is_on = True

start_time = time.time()


clo = bullet.bully.clone()

while game_is_on:
    current_time = time.time()
    elapsed_time = int(current_time) - int(start_time)
    x = ship.xcor()
    y = ship.ycor()
    bullet.goto(x, y)

    if bullet.bully.distance(ship) < 20 or clo.distance(ship) < 20:
        print("You Loose")
        break

    if bullet.bull.ycor() > 300:
        bullet.bull.color("black")
        bullet.bull.goto(x - 100, y - 100)
    if bullet.bull.ycor() > -250:
        bullet.bull.color("white")
        bullet.bull.forward(.3)

    for i in blocks:
        if i.ycor() < -250:
            flag = False
            print("YOU LOOSE")
            break
        elif bullet.bull.distance(i) < 20:
            i.goto(900, 900)
            bullet.bull.goto(0, -350)
    if flag is False:
        break

    if all(i.ycor() > 600 for i in blocks):
        print("You Win")
        break

    running = True
    bombs()
    bombs2()
    running = False

    if elapsed_time % 5 != 0:
        bullet.bully.forward(.3)
        clo.forward(.3)

    else:
        bullet.bully.goto(i.xcor() - 150, i.ycor())
        clo.goto(i.xcor() - 475, i.ycor())


    screen.update()
screen.exitonclick()
