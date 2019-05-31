# from importlib import reload
# import zDogPy.boilerplate
# reload(zDogPy.boilerplate)
# import zDogPy.illustration
# reload(zDogPy.illustration)
# import zDogPy.box
# reload(zDogPy.box)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.box import Box

D = 20
c1 = 1, 0, 0, 0.5 # True
c2 = 0, 1, 0, 0.5 # True
c3 = 0, 0, 1, 0.5 # True

I = Illustration()
I.centered = True
I.setSize(50, 50)

B = Box(addTo=I,
    stroke=5,
    fill=True,
    color=(1, 0, 0, 0.5),
    width=D, 
    height=D, 
    depth=D,
    topFace=c1,
    rearFace=c2,
    leftFace=c3,
    rightFace=c3,
    frontFace=c2,
    bottomFace=c1,
)

I.showInterface()
I.updateRenderGraph()
