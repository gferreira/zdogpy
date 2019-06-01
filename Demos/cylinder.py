from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.cylinder
reload(zDogPy.cylinder)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.cylinder import Cylinder

I = Illustration()
I.setSize(100, 100)

gold   = '#EA0'
garnet = '#C25'

C = Cylinder(addTo=I,
    diameter=5,
    length=30,
    translate={ 'x': 4, 'y': -4 },
    rotate={ 'x': TAU/4 },
    color=gold,
    backface=garnet,
    stroke=10)

I.showInterface()
I.updateRenderGraph()
