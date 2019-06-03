from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.rect import Rect
from zDogPy.shape import Shape
from zDogPy.illustration import Illustration

I = Illustration()
I.setSize(200, 200)

gold = '#EA0'
eggplant = '#636'
garnet = '#C25'

rect = Rect(
    addTo=I,
    width=64,
    height=64,
    translate={ 'x' : -48 },
    stroke=16,
    color=gold)

Shape(
    addTo=rect,
    translate={ 'z' : 20 },
    stroke=32,
    color=eggplant,
)

rect.copyGraph(
    translate={ 'x': 48 }, # buggy
    color=garnet,
)

I.showInterface()
I.updateRenderGraph()

# print(I.children)
