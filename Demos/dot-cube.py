# from importlib import reload
# import zDogPy.illustration
# reload(zDogPy.illustration)
# import zDogPy.boilerplate
# reload(zDogPy.boilerplate)
# import zDogPy.anchor
# reload(zDogPy.anchor)
# import zDogPy.vector
# reload(zDogPy.vector)
# import zDogPy.shape
# reload(zDogPy.shape)

from zDogPy.boilerplate import TAU
from zDogPy.anchor import Anchor
from zDogPy.vector import Vector
from zDogPy.shape import Shape
from zDogPy.illustration import Illustration

I = Illustration()
I.setSize(24, 24)

D = 5
S = 3

origin = Anchor(addTo=I, scale=3)
dotOptions = dict(addTo=origin, stroke=S, color=(1, 0, 0, 0.5))

# Shape(translate={ 'x':  0, 'y' :  0, 'z':  0 }, **dotOptions)

Shape(translate={ 'x':  D, 'y' :  D, 'z':  D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' :  D, 'z':  D }, **dotOptions)
Shape(translate={ 'x':  D, 'y' : -D, 'z':  D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' : -D, 'z':  D }, **dotOptions)

Shape(translate={ 'x':  0, 'y' :  D, 'z':  D }, **dotOptions)
Shape(translate={ 'x':  0, 'y' : -D, 'z':  D }, **dotOptions)
Shape(translate={ 'x':  0, 'y' :  D, 'z': -D }, **dotOptions)
Shape(translate={ 'x':  0, 'y' : -D, 'z': -D }, **dotOptions)

Shape(translate={ 'x':  D, 'y' :  D, 'z': -D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' :  D, 'z': -D }, **dotOptions)
Shape(translate={ 'x':  D, 'y' : -D, 'z': -D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' : -D, 'z': -D }, **dotOptions)

Shape(translate={ 'x':  D, 'y' :  0, 'z': -D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' :  0, 'z': -D }, **dotOptions)
Shape(translate={ 'x':  D, 'y' :  0, 'z':  D }, **dotOptions)
Shape(translate={ 'x': -D, 'y' :  0, 'z':  D }, **dotOptions)

Shape(translate={ 'x':  D, 'y' :  D, 'z':  0 }, **dotOptions)
Shape(translate={ 'x': -D, 'y' :  D, 'z':  0 }, **dotOptions)
Shape(translate={ 'x':  D, 'y' : -D, 'z':  0 }, **dotOptions)
Shape(translate={ 'x': -D, 'y' : -D, 'z':  0 }, **dotOptions)

I.showInterface()
I.updateRenderGraph()
