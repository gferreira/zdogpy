'''Shape'''

from importlib import reload
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.pathCommand
reload(zDogPy.pathCommand)
import zDogPy.vector
reload(zDogPy.vector)

from zDogPy.anchor import Anchor
from zDogPy.boilerplate import TAU, hexToRGB
from zDogPy.pathCommand import PathCommand
from zDogPy.vector import Vector

class Shape(Anchor):

    actionNames = [
      'move',
      'line',
      'bezier',
      'arc',
    ]

    pathCommands = []

    def __init__(self, stroke=1, fill=False, color=(0, 1, 0), closed=True, visible=True, path=[{'x':0}], front=dict(z=1), backface=True, **kwargs):
        Anchor.__init__(self, **kwargs)

        self.stroke   = stroke
        self.fill     = fill
        self.color    = color
        self.closed   = closed
        self.visible  = visible
        self.path     = path
        self.backface = backface

        self.updatePath()

        self.front = Vector(**front)
        self.renderFront  = Vector(self.front)
        self.renderNormal = Vector()

    def __repr__(self):
        return '<zDog Shape>'

    def updatePath(self):
        self.setPath()
        self.updatePathCommands()

    def setPath(self):
        pass

    def updatePathCommands(self):
        '''Parse path into PathCommands.'''

        previousPoint = None

        if not self.path:
            return

        self.pathCommands = []

        for i, pathPart in enumerate(self.path):

            # pathPart can be just vector coordinates -> { x, y, z }
            # or path instruction -> { arc: [ {x0,y0,z0}, {x1,y1,z1} ] }
            keys   = pathPart.keys()
            method = list(keys)[0]
            points = pathPart[method]

            # default to line if no instruction
            isInstruction = len(keys) == 1 and method in self.actionNames
            if not isInstruction:
                method = 'line'
                points = pathPart

            # munge single-point methods like line & move without arrays
            isLineOrMove  = method == 'line' or method == 'move'
            isPointsArray = isinstance(points, list)
            if isLineOrMove and not isPointsArray:
                points = [points]

            # first action is always move
            if i == 0:
                method = 'move'
            # arcs require previous last point
            command = PathCommand(method, points, previousPoint)
            # update previousLastPoint
            previousPoint = command.endRenderPoint

            self.pathCommands.append(command)

    # ------
    # update
    # ------

    def reset(self):
        self.renderOrigin.set(self.origin)
        self.renderFront.set(self.front)
        # reset command render points
        for command in self.pathCommands:
            command.reset()

    def transform(self, translation, rotation, scale):
        # calculate render points backface visibility & cone/hemisphere shapes
        self.renderOrigin.transform(translation, rotation, scale)
        self.renderFront.transform(translation, rotation, scale)
        self.renderNormal.set(self.renderOrigin).subtract(self.renderFront)

        # transform points
        for command in self.pathCommands:
            command.transform(translation, rotation, scale)

        # transform children
        for child in self.children:
            child.transform(translation, rotation, scale)

    def updateSortValue(self):
        if not len(self.pathCommands):
            return
        sortValueTotal = 0
        for command in self.pathCommands:
            sortValueTotal += command.endRenderPoint.z
        # average sort value of all points
        # def not geometrically correct, but works for me
        self.sortValue = sortValueTotal / len(self.pathCommands)

    # ------
    # render
    # ------

    def getLineWidth(self):
        if not self.stroke:
            return 0
        if self.stroke == True:
            return 1
        return self.stroke

    def getRenderColor(self):
        # use backface color if applicable
        isBackfaceColor = isinstance(self.backface, str) and self.isFacingBack
        color = self.backface if isBackfaceColor else self.color

        if type(color) is str:
            color = hexToRGB(color)

        return color

    def render(self, ctx, renderer):

        length = len(self.pathCommands)
        if not self.visible or not length:
            return

        # do not render if hiding backface
        self.isFacingBack = self.renderNormal.z > 0
        if not self.backface and not self.isFacingBack:
            return

        if not renderer:
            print(f'Zdog renderer required. Set to {renderer}')

        # render dot or path
        isDot = length == 1
        if isDot:
            self.renderDot(ctx, renderer)
        else:
            self.renderPath(ctx, renderer)

    def renderDot(self, ctx, renderer):

        # render lines with no size as circle
        lineWidth = self.getLineWidth()
        if not lineWidth:
            return

        color  = self.getRenderColor()
        point  = self.pathCommands[0].endRenderPoint
        radius = lineWidth / 2

        renderer.stroke(False, color, self.getLineWidth())
        renderer.fill(True, color)
        ctx.oval(point.x - radius, point.y - radius, radius * 2, radius * 2)

    def renderPath(self, ctx, renderer):

        isTwoPoints = len(self.pathCommands) == 2 and self.pathCommands[1].method == 'line'
        isClosed = not isTwoPoints and self.closed
        color = self.getRenderColor()

        renderer.stroke(self.stroke, color, self.getLineWidth())
        renderer.fill(self.fill, color)
        renderer.renderPath(self.pathCommands, isClosed)
        renderer.end()
