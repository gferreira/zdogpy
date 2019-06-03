from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor
from zDogPy.ellipse import Ellipse
from zDogPy.shape import Shape

I = Illustration()
I.setSize(200, 200)

orange   = '#E62'
eggplant = '#636'

# read transform from attribute and set anchor
anchorOptions = { 'addTo': I }

anchor = Anchor(**anchorOptions)

# circle
Ellipse(
    addTo=anchor,
    diameter=80,
    translate={ 'z' : -40 },
    stroke=20,
    color=eggplant,
)

# triangle
Shape(
    addTo=anchor,
    path=[
        { 'x' :   0, 'y' : -32 },
        { 'x' :  32, 'y' :  32 },
        { 'x' : -32, 'y' :  32 },
    ],
    translate={ 'z' : 40 },
    color=orange,
    stroke=12,
    fill=True)

I.showInterface()
I.updateRenderGraph()
