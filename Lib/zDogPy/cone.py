'''Cone composite shape'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.vector
reload(zDogPy.vector)
import zDogPy.pathCommand
reload(zDogPy.pathCommand)
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.ellipse
reload(zDogPy.ellipse)

from math import sin, cos, acos, atan2
from zDogPy.boilerplate import TAU
from zDogPy.vector import Vector
from zDogPy.pathCommand import PathCommand
from zDogPy.anchor import Anchor
from zDogPy.ellipse import Ellipse

class Cone(Ellipse):

    length = 1
    fill   = True

    def __init__(self, **kwargs):

        if 'length' in kwargs:
            self.length = kwargs['length']

        Ellipse.__init__(self, **kwargs)

        # composite shape, create child shapes
        self.apex = Anchor(
            addTo=self,
            translate={ 'z': self.length },
        )

        # vectors used for calculation
        self.renderApex = Vector()
        self.tangentA   = Vector()
        self.tangentB   = Vector()

        self.surfacePathCommands = [
            # points set in renderConeSurface
            PathCommand('move', [{}], None),
            PathCommand('line', [{}], None),
            PathCommand('line', [{}], None),
        ]

    def __repr__(self):
        return '<zDogPy Cone>'

    def render(self, ctx, renderer):
        self.renderConeSurface(ctx, renderer)
        Ellipse.render(self, ctx, renderer)

    def renderConeSurface(self, ctx, renderer):
        if not self.visible:
            return

        self.renderApex.set(self.apex.renderOrigin)
        self.renderApex.subtract(self.renderOrigin)

        scale          = self.renderNormal.magnitude()
        apexDistance   = self.renderApex.magnitude2d()
        normalDistance = self.renderNormal.magnitude2d()

        # eccentricity
        eccenAngle = acos(normalDistance / scale)
        eccen      = sin(eccenAngle)
        radius     = self.diameter / 2 * scale

        # does apex extend beyond eclipse of face
        isApexVisible = radius * eccen < apexDistance
        if not isApexVisible:
            return

        # update tangents
        apexAngle     = atan2(self.renderNormal.y, self.renderNormal.x ) + TAU / 2
        projectLength = apexDistance / eccen
        projectAngle  = acos(radius / projectLength)

        # set tangent points
        tangentA = self.tangentA
        tangentB = self.tangentB

        tangentA.x = cos(projectAngle) * radius * eccen
        tangentA.y = sin(projectAngle) * radius

        tangentB.set(self.tangentA)
        tangentB.y *= -1

        tangentA.rotateZ(apexAngle)
        tangentB.rotateZ(apexAngle)
        tangentA.add(self.renderOrigin)
        tangentB.add(self.renderOrigin)

        self.setSurfaceRenderPoint(0, tangentA)
        self.setSurfaceRenderPoint(1, self.apex.renderOrigin)
        self.setSurfaceRenderPoint(2, tangentB)

        # render
        renderer.stroke(self.stroke, self.color, self.getLineWidth())
        renderer.fill(self.fill, self.color)
        renderer.begin()
        renderer.renderPath(self.surfacePathCommands)
        renderer.end()

    def setSurfaceRenderPoint(self, index, point):
        renderPoint = self.surfacePathCommands[index].renderPoints[0]
        renderPoint.set(point)
