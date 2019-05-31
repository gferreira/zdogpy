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
illo.setSize(100, 100)

anchor = Anchor(addTo=illo, translate={'y': 10})
rect = Rect(addTo=anchor, width=80, height=60, rotate={'y': -2}, color=(0, 0, 1))

print(rect.rotate.y)

rect.rotate.y = 3
print(rect.rotate.y)

illo.updateRenderGraph()
