'''Polygon'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.shape
reload(zDogPy.shape)

from math import sin, cos
from zDogPy.boilerplate import TAU
from zDogPy.shape import Shape

class Polygon(Shape):

    def __init__(self, sides=3, radius=0.5, **kwargs):
        self.sides  = sides
        self.radius = radius
        Shape.__init__(self, **kwargs)

    def __repr__(self):
        return '<zDog Polygon>'

    def setPath(self):
        self.path = []
        for i in range(self.sides):
            theta = i / self.sides * TAU - TAU / 4
            x = cos(theta) * self.radius
            y = sin(theta) * self.radius
            self.path.append({ 'x': x, 'y': y })
        return self
