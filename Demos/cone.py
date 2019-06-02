from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.cone
reload(zDogPy.cone)
import zDogPy.ellipse
reload(zDogPy.ellipse)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.cone import Cone
from zDogPy.ellipse import Ellipse

I = Illustration()
I.setSize(100, 100)

gold   = '#EA0'
garnet = '#C25'

C = Cone(addTo=I,
    diameter=16,
    length=20,
    translate={ 'z': 1 },
    # rotate={ 'x': TAU/4 },
    fill=True,
    color=gold,
    closed=True,
    backface=garnet,
    stroke=5)

I.showInterface()
I.updateRenderGraph()
