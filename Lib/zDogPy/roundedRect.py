'''RoundedRect'''


from importlib import reload
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.shape import Shape

class RoundedRect(Shape):

    def __init__(self, width=1, height=1, cornerRadius=0.25, closed= False, **kwargs):
        self.width  = width  if width  is not None else 1
        self.height = height if height is not None else 1
        self.cornerRadius = cornerRadius
        self.closed = closed
        Shape.__init__(self, **kwargs)

    def __repr__(self):
        return f'<zDog RoundedRect {self.width} {self.height}>'

    def setPath(self):
        xA = self.width / 2
        yA = self.height / 2
        shortSide    = min(xA, yA)
        cornerRadius = min(self.cornerRadius, shortSide)
        xB = xA - cornerRadius
        yB = yA - cornerRadius

        path = [
            # top right corner
            { 'x' : xB, 'y' : -yA },
            { 'arc' : [
              { 'x' : xA, 'y' : -yA },
              { 'x' : xA, 'y' : -yB },
            ]},
        ]

        # bottom right corner
        if yB:
            path.append({ 'x' : xA, 'y' : yB })
            path.append({ 'arc' : [
                { 'x' : xA, 'y' :  yA },
                { 'x' : xB, 'y' :  yA },
            ]})

        # bottom left corner
        if xB:
            path.append({ 'x' : -xB, 'y' : yA })
            path.append({ 'arc' : [
                { 'x' : -xA, 'y' : yA },
                { 'x' : -xA, 'y' : yB },
            ]})

        # top left corner
        if yB:
            path.append({ 'x' : -xA, 'y' : -yB })
            path.append({ 'arc' : [
                { 'x' : -xA, 'y' : -yA },
                { 'x' : -xB, 'y' : -yA },
            ]})

        # back to top right corner
        if xB:
            path.append({ 'x' : xB, 'y' : -yA })

        self.path = path

def updateSortValue(self):
    Shape.updateSortValue(self)
    # ellipse is self closing, do not count last point twice
    length = len(self.pathCommands)
    lastPoint = self.pathCommands[length - 1].endRenderPoint
    self.sortValue -= lastPoint.z / length
