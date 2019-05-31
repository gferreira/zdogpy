from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor 
from zDogPy.rect import Rect 

illo = Illustration()
illo.centered = True
illo.setSize(100, 100)

anchor = Anchor(addTo=illo, translate={'y': 8})

zRect = Rect(addTo=anchor, rotate=TAU/4, width=20, height=20, color=(1, 0, 0))
xRect = Rect(addTo=zRect, translate={ 'x':  40 }, width=20, height=20, color=(0, 1, 0))
yRect = Rect(addTo=xRect, translate={ 'y': -60 }, width=20, height=20, color=(0, 0, 1))

Variable([
    dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
], globals())

illo.rotate.x = rotateX
illo.rotate.y = rotateY
illo.rotate.z = rotateZ

illo.updateRenderGraph()
