from importlib import reload
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.shape
reload(zDogPy.shape)

from zDogPy.illustration import Illustration
from zDogPy.shape import Shape

# eggplant = 1, 1, 0.5

illo = Illustration()
illo.centered = True
illo.setSize(40, 40)

# lines
S1 = Shape(
    addTo=illo,
    path=[
        { 'x': -6, 'y': -6 },
        { 'x':  6, 'y': -6 },
        { 'x':  6, 'y':  6 },
        { 'x': -6, 'y':  6 },
    ],
    translate={ 'x': -12, 'y': -12 },
    closed=True,
    color=(1, 0, 0),
    stroke=2)

# move
S2 = Shape(
    addTo=illo,
    path=[
        { 'x': -6, 'y': -6 },
        { 'x':  6, 'y': -6 },
        { 'move': { 'x': -6, 'y':  6 } },
        { 'x':  6, 'y':  6 },
    ],
    translate={ 'x': 12, 'y': -12 },
    closed=False,
    color=(0, 1, 0),
    stroke=3)

# arc
# S3 = Shape(
#     addTo=illo,
#     path=[
#         { 'x': -6, 'y': -6 }, # start
#         { 'arc': [
#             { 'x':  2, 'y': -6 }, # corner
#             { 'x':  2, 'y':  2 }, # end point
#         ]},
#         { 'arc': [ # start next arc from last end point
#             { 'x':  2, 'y':  6 }, # corner
#             { 'x':  6, 'y':  6 }, # end point
#         ]},
#     ],
#     translate={ 'x': -12, 'y': 12 },
#     closed=False,
#     color=(0, 0, 1),
#     stroke=2)

# bezier
S4 = Shape(
    addTo=illo,
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
    color=(1, 0, 1),
    stroke=2)

# animate

Variable([
    dict(name="rotateX", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateY", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
    dict(name="rotateZ", ui="Slider", args=dict(value=0, minValue=0, maxValue=2*pi)),
], globals())

illo.rotate.x = rotateX
illo.rotate.y = rotateY
illo.rotate.z = rotateZ

illo.updateRenderGraph()