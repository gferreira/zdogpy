from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor 
from zDogPy.rect import Rect 

illo = Illustration()
illo.setSize(10, 10)

anchor = Anchor(addTo=illo, translate={'y': 2})
rect = Rect(addTo=anchor)

illo.updateRenderGraph()
