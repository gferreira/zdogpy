from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.rect
reload(zDogPy.rect)
import zDogPy.ellipse
reload(zDogPy.ellipse)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.rect import Rect
from zDogPy.ellipse import Ellipse

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(240, 240)

E = Ellipse(addTo=I,
    diameter=80,
    stroke=20,
    color='#636',
    fill=False,
    translate=dict(z=40))

R = Rect(addTo=I,
    width=80,
    height=80,
    stroke=12,
    color='#E62',
    fill=True,
    translate=dict(z=-40))

I.showInterface()
I.updateRenderGraph()
