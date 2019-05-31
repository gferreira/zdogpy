'''Ellipse'''

from importlib import reload
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.shape import Shape

class Ellipse(Shape):

    def __init__(self, diameter=1, width=None, height=None, quarters=4, closed=False, **kwargs):
        self.diameter = diameter
        self.width    = width
        self.height   = height
        self.quarters = quarters
        self.closed   = closed
        Shape.__init__(self, **kwargs)

    def __repr__(self):
        return '<zDog Ellipse>'

    def setPath(self):
        width  = self.width  if self.width  else self.diameter
        height = self.height if self.height else self.diameter
        x = width  / 2
        y = height / 2
        self.path = [
            { 'x': 0, 'y': -y },
            { 'arc': [
                { 'x': x, 'y': -y },
                { 'x': x, 'y': 0 },
            ]},
        ]
        # bottom right
        if self.quarters > 1:
            self.path += [{'arc': [
                    { 'x': x, 'y': y },
                    { 'x': 0, 'y': y },
                ]}]
        # bottom left
        if self.quarters > 2:
            self.path += [{'arc': [
                    { 'x': -x, 'y': y },
                    { 'x': -x, 'y': 0 },
                ]}]
        # top left
        if self.quarters > 3:
            self.path += [{'arc': [
                    { 'x': -x, 'y': -y },
                    { 'x': 0,  'y': -y },
                ]}]

    def updateSortValue(self):
        Shape.updateSortValue(self)
        if self.quarters != 4:
            return
        # ellipse is self closing, do not count last point twice
        length = len(self.pathCommands)
        lastPoint = self.pathCommands[length-1].endRenderPoint
        self.sortValue -= lastPoint.z / length
