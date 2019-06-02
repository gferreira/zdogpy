'''Glyph'''

from importlib import reload
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.shape import Shape

def makePath(glyph):
    path = []
    for ci, c in enumerate(glyph.contours):
        pt0 = c[-1][-1]
        cmd = { 'move' : {'x': pt0.x, 'y': pt0.y } }
        path.append(cmd)
        for si, s in enumerate(c.segments):
            if not len(s) == 3:
                pt = s[0]
                cmd = { 'x': pt.x, 'y': pt.y }
            else:
                cmd = { 'bezier' : [{ 'x': pt.x, 'y': pt.y } for pt in s] }
            path.append(cmd)
    return path

class Glyph(Shape):

    def __init__(self, glyph, centered=True, **kwargs):
        self.glyph = glyph
        if centered:
            L, B, R, T = self.glyph.bounds
            x = L + (R - L) / 2
            y = B + (T - B) / 2
            kwargs['translate'] = { 'x' : -x, 'y': -y }
        Shape.__init__(self, **kwargs)
        self.updatePath()

    def setPath(self):
        self.path = makePath(self.glyph)

    def render(self, ctx, renderer):
        Shape.render(self, ctx, renderer)
