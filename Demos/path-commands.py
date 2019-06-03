# from importlib import reload
# import zDogPy.illustration
# reload(zDogPy.illustration)
# import zDogPy.shape
# reload(zDogPy.shape)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.shape import Shape

eggplant = '#636'

I = Illustration()
I.color = '#FDB'
I.centered = True
I.setSize(60, 60)

# lines
S1 = Shape(addTo=I,
    path=[
        { 'x': -6, 'y': -6 },
        { 'x':  6, 'y': -6 },
        { 'x':  6, 'y':  6 },
        { 'x': -6, 'y':  6 },
    ],
    translate={ 'x': -12, 'y': -12 },
    closed=False,
    color=eggplant,
    stroke=2)

# move
S2 = Shape(addTo=I,
    path=[
        { 'x': -6, 'y': -6 },
        { 'x':  6, 'y': -6 },
        { 'move': { 'x': -6, 'y':  6 } },
        { 'x':  6, 'y':  6 },
    ],
    translate={ 'x': 12, 'y': -12 },
    closed=False,
    color=eggplant,
    stroke=2)

# arc
S3 = Shape(addTo=I,
    path=[
        { 'x': -6, 'y': -6 }, # start
        { 'arc': [
            { 'x':  2, 'y': -6 }, # corner
            { 'x':  2, 'y':  2 }, # end point
        ]},
        { 'arc': [ # start next arc from last end point
            { 'x':  2, 'y':  6 }, # corner
            { 'x':  6, 'y':  6 }, # end point
        ]},
    ],
    translate={ 'x': -12, 'y': 12 },
    closed=False,
    color=eggplant,
    stroke=2)

# bezier
S4 = Shape(addTo=I,
    path=[
        { 'x': -6, 'y': -6 }, # start
        { 'bezier': [
            { 'x':  2, 'y': -6 }, # start control point
            { 'x':  2, 'y':  6 }, # end control point
            { 'x':  6, 'y':  6 }, # end control point
        ]},
    ],
    translate={ 'x': 12, 'y': 12 },
    closed=False,
    color=eggplant,
    stroke=2)

I.showInterface()
I.updateRenderGraph()
