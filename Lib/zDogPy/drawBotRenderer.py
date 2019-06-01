'''DrawBotRenderer'''

import drawBot as ctx
from zDogPy.boilerplate import hexToRGB

class DrawBotRenderer:

    isDrawBot = True

    def __init__(self):
        self.ctx = ctx

    def __repr__(self):
        return f'<zDog DrawBotRenderer>'

    def begin(self):
        ctx.newPath()

    def move(self, point):
        ctx.moveTo((point.x, point.y))

    def line(self, point):
        ctx.lineTo((point.x, point.y))

    def bezier(self, cp0, cp1, end):
        ctx.curveTo((cp0.x, cp0.y), (cp1.x, cp1.y), (end.x, end.y))

    def closePath(self):
        ctx.closePath()

    def setPath(self):
        pass

    def renderPath(self, pathCommands, isClosed=True):

        self.begin()
        for command in pathCommands:
            command.render(ctx, self)

        if isClosed:
            self.closePath()

        ctx.drawPath()

    def stroke(self, isStroke, color, lineWidth, lineCap='round', lineJoin='round'):
        if not isStroke:
            ctx.stroke(None)
            return

        if type(color) is str and color.startswith('#'):
            color = hexToRGB(color)

        ctx.strokeWidth(lineWidth)
        ctx.stroke(*color)
        ctx.lineCap(lineCap)
        ctx.lineJoin(lineJoin)

    def fill(self, isFill, color):
        if not isFill:
            ctx.fill(None)
            return

        if type(color) is str and color.startswith('#'):
            color = hexToRGB(color)

        ctx.fill(*color)

    def end(self):
        pass
