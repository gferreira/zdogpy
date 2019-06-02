from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.roundedRect
reload(zDogPy.roundedRect)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.roundedRect import RoundedRect

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(40, 40)

options = {
    'addTo': I,
    'width': 20,
    'height': 20,
    'cornerRadius': 4,
    'stroke': 2,
    'fill': False,
    'rotate': dict(x=TAU/2),
}

RoundedRect(color='#636', translate=dict(z=5), **options)
RoundedRect(color='#E62', translate=dict(z=-5), **options)

I.showInterface()
I.updateRenderGraph()
