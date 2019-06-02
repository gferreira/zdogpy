# run this demo in RF DrawBot with a font open

from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.shape import Shape

eggplant = '#636'

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(1000, 1000)

g = CurrentGlyph()
L, B, R, T = g.bounds
x = (R - L) / 2
y = (T - B) / 2

path = []
for ci, c in enumerate(g.contours):
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
    
# print(path)

glyph = Shape(addTo=I,
    path=path,
    translate={ 'x': -x, 'y': -y },
    closed=False,
    color=eggplant,
    fill=False,
    stroke=20)

I.showInterface()
I.updateRenderGraph()
