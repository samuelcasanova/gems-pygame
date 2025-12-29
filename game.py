from pgzero.builtins import Actor
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('ship')
ship.x = 370
ship.y = 550


def draw():
    ship.draw()

pgzrun.go() # Must be last line