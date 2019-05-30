'''Anchor'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.vector
reload(zDogPy.vector)
import zDogPy.drawBotRenderer
reload(zDogPy.drawBotRenderer)

import drawBot as ctx
from zDogPy.vector import Vector
from zDogPy.boilerplate import TAU, extend
from zDogPy.drawBotRenderer import DrawBotRenderer

onePoint = { 'x' : 1, 'y' : 1, 'z' : 1 }

class Anchor(Vector):

    def __init__(self, rotate=None, translate=None, scale=None, addTo=None, **kwargs):

        # set defaults & options
        # self.defaults = {}
        self.addTo = addTo
        self.flatGraph = []

        # transform
        self.translate = Vector(**translate) if translate else Vector()
        self.rotate    = Vector(**rotate) if rotate else Vector()
        self.scale     = Vector(**scale) if scale else Vector()

        # origin
        self.origin       = Vector()
        self.renderOrigin = Vector()

        # children
        self.children = []
        if self.addTo:
            self.addTo.addChild(self)

    def __repr__(self):
        return '<zDog Anchor>'

    def setOptions(self, **kwargs):
        if not kwargs:
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def addChild(self, shape):
        if shape in self.children:
            shape.remove() # remove previous parent
        shape.addTo = self # keep parent reference
        self.children.append(shape)

    def removeChild(self, shape):
        index = self.children.index(shape)
        del self.children[index]

    def remove(self):
        if self.addTo:
            self.addTo.removeChild(self)

    # ------
    # update
    # ------

    def update(self):
        # update self
        self.reset()
        # update children
        for child in self.children:
            child.update()
        self.transform(self.translate, self.rotate, self.scale)

    def reset(self):
        self.renderOrigin.set(self.origin)

    def transform(self, translation, rotation, scale):

        self.renderOrigin.transform(translation, rotation, scale)

        # transform children
        for child in self.children:
            child.transform(translation, rotation, scale)

    def updateGraph(self):
        self.update()
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.updateSortValue()
        # z-sort
        # def shapeSorter(a, b):
        #     return a.sortValue - b.sortValue
        # self.flatGraph.sort() # shapeSorter

    def checkFlatGraph(self):
        if not self.flatGraph:
            self.updateFlatGraph()

    def updateFlatGraph(self):
        self.flatGraph = self.getFlatGraph()

    def getFlatGraph(self):
        # return Array of self & all child graph items
        flatGraph = [self]
        for child in self.children:
            childFlatGraph = child.getFlatGraph()
            flatGraph += childFlatGraph
        return flatGraph

    def updateSortValue(self):
        self.sortValue = self.renderOrigin.z

    # ------
    # render
    # ------

    def render(self, ctx, renderer):
        # print(f'rendering {self}...')
        pass

    def renderGraphDrawBot(self):
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.render(ctx, DrawBotRenderer())

    # ----
    # misc
    # ----

    # def copy(self):
    #     a = Anchor()
    #     a.addTo        = self.addTo
    #     a.flatGraph    = self.flatGraph
    #     a.translate    = self.translate
    #     a.rotate       = self.rotate
    #     a.scale        = self.scale
    #     a.origin       = self.origin
    #     a.renderOrigin = self.renderOrigin
    #     a.children     = self.children
    #     return a

    def copyGraph(self, options):
        # clone = self.copy(options)
        # for child in self.children:
        #     child.copyGraph({'addTo' : clone })
        # return clone
        pass

    def normalizeRotate(self):
        self.rotate.x = self.rotate.x % TAU
        self.rotate.y = self.rotate.y % TAU
        self.rotate.z = self.rotate.z % TAU

    # --------
    # subclass
    # --------

    def getSubclass(self):
        # ???
        pass


if __name__ == '__main__':

    A = Anchor()
    print(A.renderOrigin.translate, A.renderOrigin.rotate, A.renderOrigin.scale)
    A.transform(Vector(10), Vector(), Vector())
    print(A.renderOrigin.translate, A.renderOrigin.rotate, A.renderOrigin.scale)

