from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.rect import Rect

# -----
# setup
# -----

D = 20

illo = Illustration()
illo.centered = True
illo.setSize(50, 50)

frontFace = Rect(addTo=illo, width=D, height=D, stroke=None, color=(0, 1, 1), fill=True)
rearFace  = Rect(addTo=illo, width=D, height=D, stroke=None, color=(1, 0, 0), fill=True, translate=dict(z=D))
leftFace  = Rect(addTo=illo, width=D, height=D, stroke=None, color=(0, 1, 0), fill=True, rotate=dict(y=TAU/4))

# print(frontFace.translate, frontFace.rotate)
# print(rearFace.translate, rearFace.rotate)
# print(leftFace.translate, leftFace.rotate)

Variable([
    dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="translateX", ui="Slider", args=dict(value=0, minValue=-100, maxValue=100)),
    dict(name="translateY", ui="Slider", args=dict(value=0, minValue=-100, maxValue=100)),
    dict(name="translateZ", ui="Slider", args=dict(value=0, minValue=-100, maxValue=100)),
    dict(name="scaleX", ui="Slider", args=dict(value=1, minValue=1, maxValue=2)),
    dict(name="scaleY", ui="Slider", args=dict(value=1, minValue=1, maxValue=2)),
    dict(name="scaleZ", ui="Slider", args=dict(value=1, minValue=1, maxValue=2)),
], globals())

illo.rotate.x = rotateX
illo.rotate.y = rotateY
illo.rotate.z = rotateZ

illo.translate.x = translateX
illo.translate.y = translateY
illo.translate.z = translateZ

illo.scale.x = scaleX
illo.scale.y = scaleY
illo.scale.z = scaleZ

illo.updateRenderGraph()
