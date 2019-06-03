from zDogPy.illustration import Illustration
from zDogPy.shape import Shape

eggplant = '#636'
orange   = '#E62'

start        = { 'x' : -60, 'y' : -60 }
startControl = { 'x' :  20, 'y' : -60 }
endControl   = { 'x' : -20, 'y' :  60 }
end          = { 'x' :  60, 'y' :  60 }

I = Illustration()
I.setSize(200, 200)

# curve
Shape(
    addTo=I,
    path=[
      start,
      { 'bezier': [ startControl, endControl, end ] },
    ],
    closed=False,
    stroke=20,
    color=eggplant,
)

# control points
controlDot = Shape(
    addTo=I,
    translate=startControl,
    stroke=12,
    color=orange,
)
controlDot.copy(
    translate=endControl,
)

# control handles
controlLine = Shape(
    addTo=I,
    path=[ start, startControl ],
    stroke=2,
    color=orange,
)
controlLine.copy(
    path=[ end, endControl ],
)

I.showInterface()
I.updateRenderGraph()

