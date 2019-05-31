'''DrawBotRenderer'''

import drawBot as ctx
from zDogPy.boilerplate import hexToRGB

class DrawBotRenderer:

    isDrawBot = True

    # def __init__(self):
    #     pass

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

    def stroke(self, isStroke, color, lineWidth):
        if not isStroke:
            return

        if type(color) is str and color.startswith('#'):
            color = hexToRGB(color)

        ctx.strokeWidth(lineWidth)
        ctx.stroke(*color)

    def fill(self, isFill, color):
        if not isFill:
            ctx.fill(None)
            return

        if type(color) is str and color.startswith('#'):
            color = hexToRGB(color)

        ctx.fill(*color)

    def end(self):
        pass
