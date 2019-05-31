'''Illustration'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.anchor
reload(zDogPy.anchor)

import drawBot as ctx
from zDogPy.boilerplate import TAU
from zDogPy.anchor import Anchor

class Illustration(Anchor):

    element    = None
    centered   = True
    pixelRatio = 1

    width = height = 1000

    def __init__(self, **kwargs):
        Anchor.__init__(self, **kwargs)

    def __repr__(self):
        return '<zDog Illustration>'

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

    # def render(self, ctx, renderer):
    #     pass

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
        ctx.lineCap('round')
        ctx.lineJoin('round')
        ctx.save()

        if self.centered:
            centerX = self.width  / 2 # * self.pixelRatio
            centerY = self.height / 2 # * self.pixelRatio
            ctx.translate(centerX, centerY)

        # scale = self.pixelRatio
        # ctx.scale(scale, scale)

    def postrenderDrawBot(self):
        ctx.restore()
