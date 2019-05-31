'''Rect'''

from importlib import reload
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.shape import Shape

class Rect(Shape):

    def __init__(self, width=None, height=None, **kwargs):
        self.width  = width  if width  is not None else 1
        self.height = height if height is not None else 1
        Shape.__init__(self, **kwargs)

    def __repr__(self):
        return '<zDog Rect>'

    def setPath(self):
        x = self.width / 2
        y = self.height / 2
        self.path = [
            { 'x' : -x, 'y' : -y },
            { 'x' :  x, 'y' : -y },
            { 'x' :  x, 'y' :  y },
            { 'x' : -x, 'y' :  y },
        ]
        return self
