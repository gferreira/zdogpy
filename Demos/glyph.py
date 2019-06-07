# run this demo in RF DrawBot with a font open

from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.glyph
reload(zDogPy.glyph)

from zDogPy.illustration import Illustration
from zDogPy.glyph import Glyph

eggplant = '#636'

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(1000, 1000)

g = CurrentGlyph()

glyph = Glyph(addTo=I,
    translate={'x': -30}, # not working with centered mode
    glyph=g,
    centered=True,
    closed=False,
    color=eggplant,
    fill=False,
    stroke=80)

I.showInterface()
I.updateRenderGraph()
