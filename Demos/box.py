from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.box
reload(zDogPy.box)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.box import Box

orange   = '#E62'
garnet   = '#C25'
eggplant = '#636'

side = 20

I = Illustration()
I.centered = True
I.setSize(50, 50)

B = Box(addTo=I,
    stroke=3,
    fill=True,
    rotate={'x' : TAU/8, 'y' : TAU/8, 'y' : TAU/8}, 
    color=(1, 0, 0, 0.4),
    width=side, 
    height=side, 
    depth=side,
    topFace=garnet,
    rearFace=orange,
    leftFace=eggplant,
    rightFace=eggplant,
    frontFace=orange,
    bottomFace=garnet,
)

I.showInterface()
I.updateRenderGraph()
