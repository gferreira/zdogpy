from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.polygon
reload(zDogPy.polygon)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.polygon import Polygon

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(100, 100)

Polygon(addTo=I,
    sides=5,
    radius=25,
    stroke=8,
    color='#636',
    fill=True,
    rotate=dict(x=TAU/2),
    translate=dict(z=20))

I.showInterface()
I.updateRenderGraph()
