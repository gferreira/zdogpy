from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.vector
reload(zDogPy.vector)

from math import sqrt, acos
from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor
from zDogPy.cylinder import Cylinder
from zDogPy.hemisphere import Hemisphere
from zDogPy.boilerplate import TAU
from zDogPy.vector import Vector
from zDogPy.cone import Cone
from zDogPy.polygon import Polygon

sceneSize = 24
ROOT3 = sqrt(3)
ROOT5 = sqrt(5)
PHI = (1 + ROOT5) / 2

viewRotation = Vector()

eggplant = '#636'
garnet   = '#C25'
orange   = '#E62'
gold     = '#EA0'
yellow   = '#ED0'

I = Illustration()
I.setSize(sceneSize, sceneSize)

solids = []

hourglass = Anchor(
    addTo=I,
    translate={ 'x' : 0, 'y' : -4 },
)
solids.append(hourglass)

hemi = Hemisphere(
    addTo=hourglass,
    diameter=2,
    translate={ 'z': -1 },
    color=garnet,
    backface=orange,
    stroke=True,
)
# # hemi.copy(
# #     translate={ 'z': 1 },
# #     rotate={ 'y': TAU / 2 },
# #     color=eggplant,
# #     backface=gold)

sphere = Anchor(
    addTo=I,
    diameter=2,
    translate={ 'x' : -4, 'y' : -4 }
)
solids.append(sphere)

hemi = Hemisphere(
    diameter=2,
    addTo=sphere,
    color=orange,
    backface=eggplant,
    stroke=True)
# # hemi.copy(
# #     rotate={ 'y' : TAU / 2 },
# #     color=eggplant,
# #     backface=orange)


I.showInterface()
I.updateRenderGraph()
