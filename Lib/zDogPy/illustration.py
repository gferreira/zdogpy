'''Illustration'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.anchor
reload(zDogPy.anchor)

import drawBot as ctx
from zDogPy.boilerplate import TAU, hexToRGB
from zDogPy.anchor import Anchor

class Illustration(Anchor):

    element    = None
    centered   = True
    pixelRatio = 1

    width = height = 1000

    blendMode = 'normal'
    color     = None

    variables = [
        dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=TAU)),
        dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=TAU)),
        dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=TAU)),
    ]

    def __init__(self, **kwargs):
        Anchor.__init__(self, **kwargs)

    def __repr__(self):
        return '<zDogPy Illustration>'

    def setSize(self, width, height):
        width  = round(width)
        height = round(height)
        self.setSizeDrawBot(width, height)

    def setMeasuredSize(self):
        pass

    # ------
    # render
    # ------

    def renderGraph(self, item):
        self.renderGraphDrawBot(item)

    def updateRenderGraph(self, item=None):
        # combo method
        self.updateGraph()
        self.renderGraph(item)

    # -------
    # DrawBot
    # -------

    def render(self, ctx, renderer):
        pass

    def setSize(self, width, height):
        self.width  = width  * self.pixelRatio
        self.height = height * self.pixelRatio

    def renderGraphDrawBot(self, item=None):
        if item is None:
            item = self
        self.prerenderDrawBot()
        Anchor.renderGraphDrawBot(item)
        self.postrenderDrawBot()

    def prerenderDrawBot(self):

        ctx.newPage(self.width, self.height)
        if self.color is not None:
            color = hexToRGB(self.color) if type(self.color) is str and self.color.startswith('#') else self.color
            ctx.fill(*color)
            ctx.rect(0, 0, self.width, self.height)

        ctx.blendMode(self.blendMode)
        ctx.save()

        if self.centered:
            centerX = self.width  / 2 # * self.pixelRatio
            centerY = self.height / 2 # * self.pixelRatio
            ctx.translate(centerX, centerY)

        # scale = self.pixelRatio
        # ctx.scale(scale, scale)

    def postrenderDrawBot(self):
        ctx.restore()

    def showInterface(self):

        ctx.Variable(self.variables, globals())

        self.rotate.x = rotateX
        self.rotate.y = rotateY
        self.rotate.z = rotateZ
