from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.box
reload(zDogPy.box)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.box import Box

# -----
# setup
# -----

D = 20

illo = Illustration()
illo.centered = True
illo.setSize(50, 50)

box = Box(
    addTo=illo,
    stroke=2,
    fill=True,
    color=(1, 0, 0, 0.1),
    width=20, 
    height=20, 
    depth=20,
    topFace=True,
    rearFace=True,
    leftFace=True,
    rightFace=True,
    frontFace=True,
    bottomFace=True,    
)

Variable([
    dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
], globals())

illo.rotate.x = rotateX
illo.rotate.y = rotateY
illo.rotate.z = rotateZ

illo.updateRenderGraph()
