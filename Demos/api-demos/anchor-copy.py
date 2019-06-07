from importlib import reload
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.illustration import Illustration
from zDogPy.rect import Rect
from zDogPy.vector import Vector

I = Illustration()
I.setSize(200, 200)

gold   = '#EA0'
garnet = '#C25'

rect1 = Rect(
    addTo=I,
    width=64,
    height=64,
    translate={ 'z' : 32 },
    stroke=16,
    color=gold)

rect2 = rect1.copy(
    translate={ 'z' : -32 },
    color=garnet)

I.showInterface()
I.updateRenderGraph()
