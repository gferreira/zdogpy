'''Hemisphere composite shape'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.ellipse
reload(zDogPy.ellipse)
import zDogPy.vector
reload(zDogPy.vector)

from math import sin, cos, tan
from zDogPy.boilerplate import TAU
from zDogPy.ellipse import Ellipse
from zDogPy.vector import Vector

class Hemisphere(Ellipse):

    fill = True

    def __init__(self, **kwargs):
        Ellipse.__init__(self, **kwargs)

        self.updatePath()

    def render(self, ctx, renderer):
        self.renderDome(ctx, renderer)
        # call super
        Ellipse.render(self, ctx, renderer) # arguments

    def renderDome(self, ctx, renderer):
        if not self.visible:
            return

        contourAngle = math.atan2(self.renderNormal.y, self.renderNormal.x)
        domeRadius   = self.diameter / 2 # * self.renderNormal.magnitude()

        startAngle = contourAngle + TAU / 2
        endAngle   = contourAngle - TAU / 2

        a = startAngle
        pts = [
            Vector(
                x=domeRadius,
                y=0),
            Vector(
                x=domeRadius,
                y=domeRadius * 4/3 * tan(a / 4)),
            Vector(
                x=domeRadius * (cos(a) + 4/3 * tan(a / 4) * sin(a)),
                y=domeRadius * (sin(a) - 4/3 * tan(a / 4) * cos(a))),
            Vector(
                x=domeRadius * cos(a),
                y=domeRadius * sin(a)),
        ]
        pts = [p.add(self.renderOrigin) for p in pts]
        print(self.renderOrigin)

        renderer.stroke(self.stroke, self.color, self.getLineWidth())
        renderer.fill(self.fill, self.color)
        renderer.begin()
        renderer.move(pts[0])
        renderer.bezier(pts[1], pts[2], pts[3])
        # renderer.closePath()
        ctx.drawPath()
        renderer.end()


