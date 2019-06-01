'''Anchor'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.vector
reload(zDogPy.vector)
import zDogPy.drawBotRenderer
reload(zDogPy.drawBotRenderer)

from functools import cmp_to_key
import drawBot as ctx
from zDogPy.vector import Vector
from zDogPy.boilerplate import TAU
from zDogPy.drawBotRenderer import DrawBotRenderer

def shapeSorter(a, b):
    return a.sortValue - b.sortValue

class Anchor(Vector):

    def __init__(self, rotate=None, translate=None, scale=None, addTo=None, **kwargs):

        self.addTo = addTo
        self.flatGraph = []
        self.sortValue = 0

        # transform

        if translate is None:
            self.translate = Vector()
        elif isinstance(translate, Vector):
            self.translate = translate
        elif isinstance(translate, dict):
            self.translate = Vector(**translate)
        elif isinstance(translate, float) or isinstance(translate, int):
            self.translate = Vector(translate)

        if rotate is None:
            self.rotate = Vector()
        elif isinstance(translate, Vector):
            self.rotate = Vector(**rotate)
        elif isinstance(rotate, dict):
            self.rotate = Vector(**rotate)
        elif isinstance(rotate, float) or isinstance(rotate, int):
            self.rotate = Vector(rotate)

        if scale is None:
            self.scale = Vector()
        elif isinstance(translate, Vector):
            self.scale = Vector(**scale)
        elif isinstance(scale, dict):
            self.scale = Vector(**scale)
        elif isinstance(scale, float) or isinstance(scale, int):
            self.scale = Vector(scale)

        # origin
        self.origin = Vector()
        self.renderOrigin = Vector()

        # children
        self.children = []
        if self.addTo:
            self.addTo.addChild(self)

    def __repr__(self):
        return f'<zDog Anchor {self.x} {self.y} {self.z}>'

    def setOptions(self, options):
        if not options:
            return
        for key, value in options.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def addChild(self, shape):
        if shape in self.children:
            # remove previous parent
            shape.remove()
        # keep parent reference
        shape.addTo = self
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
        for i, child in enumerate(self.children):
            child.transform(translation, rotation, scale)

    def updateGraph(self):
        self.update()
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.updateSortValue()
        # z-sort
        self.flatGraph.sort(key=cmp_to_key(shapeSorter))

    def checkFlatGraph(self):
        if not self.flatGraph:
            self.updateFlatGraph()

    def updateFlatGraph(self):
        self.flatGraph = self.getFlatGraph()

    def getFlatGraph(self):
        # return list of self & all child graph items
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
        pass

    def renderGraphDrawBot(self):
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.render(ctx, DrawBotRenderer())

    # ----
    # misc
    # ----

    # def copy(self):
    #     pass

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

    # def getSubclass(self):
    #     pass
