from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.rect
reload(zDogPy.rect)
import zDogPy.ellipse
reload(zDogPy.ellipse)

from math import pi
from zDogPy.illustration import Illustration
from zDogPy.rect import Rect
from zDogPy.ellipse import Ellipse

illo = Illustration()
illo.setSize(50, 50)

Ellipse(addTo=illo, diameter=20, translate=dict(z=10), stroke=5, color=(1, 0, 0), fill=False)
Rect(addTo=illo, width=20, height=20, stroke=3, color=(0, 1, 1), fill=True, translate=dict(z=-10))

Variable([
    dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="translateX", ui="Slider", args=dict(value=0, minValue=-100, maxValue=100)),
    dict(name="scaleX", ui="Slider", args=dict(value=1, minValue=1, maxValue=2)),
    dict(name="scaleY", ui="Slider", args=dict(value=1, minValue=1, maxValue=2)),
], globals())

illo.rotate.x = rotateX
illo.rotate.y = rotateY
illo.rotate.z = rotateZ

illo.translate.x = translateX
illo.scale.x = scaleX
illo.scale.y = scaleY

illo.updateRenderGraph()

