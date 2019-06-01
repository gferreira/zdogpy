from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.hemisphere
reload(zDogPy.hemisphere)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor
from zDogPy.hemisphere import Hemisphere

yellow = '#ED0'
gold   = '#EA0'
orange = '#E62'
garnet = '#C25'

I = Illustration()
I.setSize(400, 400)

burger = Anchor(addTo=I, translate={ 'y': 0 }, )

hemisphere = Hemisphere(
    addTo=burger,
    diameter=100,
    translate={ 'x': 70, 'y': 10, 'z' : 24 },
    stroke=5,
    fill=False,
    color=orange,
)

I.showInterface()
I.updateRenderGraph()
