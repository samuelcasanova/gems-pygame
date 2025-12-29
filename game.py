from pgzero.builtins import Actor
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('ship')
ship.x = 370
ship.y = 550

gem = Actor('gem')
gem.x = 350
gem.y = 0

score = 0
game_over = False

def update():
    global score, game_over
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 5 + score / 5

    if gem.y > HEIGHT:
        game_over = True

    if gem.colliderect(ship):
        score += 1
        gem.y = 0
        gem.x = random.randint(20,WIDTH-20)

def draw():
    screen.fill((20,20,20))
    if game_over:
        screen.draw.text('Game Over', (300, 250), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (280, 300), color=(255,255,255), fontsize=60)
    else:
        ship.draw()
        gem.draw()
        screen.draw.text(f"Score: {str(score)}", (15,10), color='white', fontsize=30)

pgzrun.go() # Must be last line