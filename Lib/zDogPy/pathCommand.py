'''PathCommand'''

from importlib import reload
import zDogPy.vector
reload(zDogPy.vector)

from zDogPy.vector import Vector

def mapVectorPoint(point):
    if isinstance(point, Vector):
        return point
    else:
        return Vector(**point)

def mapNewVector(point):
    return Vector(**point)

class PathCommand:

    def __init__(self, method, points, previousPoint):
        self.method = method
        self.points = [mapVectorPoint(point) for point in points]
        self.renderPoints = [mapNewVector(point) for point in points]
        self.previousPoint = previousPoint
        self.endRenderPoint = self.renderPoints[len(self.renderPoints) - 1]
        # arc actions come with previous point & corner point
        # but require bezier control points
        if method == 'arc':
            self.controlPoints = [Vector(), Vector()]

    def __repr__(self):
        return f'<zDog PathCommand {self.method}>'

    def reset(self):
        # reset renderPoints back to original points position
        points = self.points
        for i, renderPoint in enumerate(self.renderPoints):
            point = points[i]
            renderPoint.set(point)

    def transform(self, translation, rotation, scale):
        # print(translation, rotation, scale)
        # print(self.renderPoints)
        renderPoints = []
        for renderPoint in self.renderPoints:
            # print(renderPoint)
            pt = renderPoint.copy()
            pt.transform(translation, rotation, scale)
            # print(pt)
            renderPoints.append(pt)
        self.renderPoints = renderPoints
        # print(renderPoints)
        print()

    def render(self, ctx, renderer):
        cmd = getattr(self, self.method)
        return cmd(ctx, renderer)

    def move(self, ctx, renderer):
        return renderer.move(self.renderPoints[0])

    def line(self, ctx, renderer):
        return renderer.line(self.renderPoints[0])

    def bezier(self, ctx, renderer):
        cp0 = self.renderPoints[0]
        cp1 = self.renderPoints[1]
        end = self.renderPoints[2]
        return renderer.bezier(cp0, cp1, end)

    def arc(self, ctx, renderer):
        prev   = self.previousPoint
        corner = self.renderPoints[0]
        end = self.renderPoints[1]
        cp0 = self.controlPoints[0]
        cp1 = self.controlPoints[1]
        cp0.set(prev).lerp(corner, 9/16)
        cp1.set(end).lerp(corner, 9/16)
        return renderer.bezier(cp0, cp1, end)
