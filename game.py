from pgzero.builtins import Actor
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('ship3')
ship.x = 370
ship.y = 550
ship.scale = 0.2

box = Rect((20, 20), (50, 50))

def draw():
    screen.draw.filled_rect(box, "red")
    # screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    ship.draw()

pgzrun.go() # Must be last line