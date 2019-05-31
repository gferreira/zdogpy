from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.box
reload(zDogPy.box)

from zDogPy.boilerplate import TAU
from zDogPy.anchor import Anchor
from zDogPy.shape import Shape
from zDogPy.illustration import Illustration
from zDogPy.box import Box

# colors
yellow   = '#ED0'
gold     = '#EA0'
orange   = '#E62'
garnet   = '#C25'
eggplant = '#636'

I = Illustration()
I.color = '#FDB'
I.setSize(120, 120)

model = Anchor(addTo=I)

D = 20

boxOptions = {
    'addTo'  : model,
    # 'stroke' : 0,
    'fill'   : True,
    'color'  : (1, 0, 0, 0.5),
    'width'  : D, 
    'height' : D, 
    'depth'  : D,
    'topFace'    : yellow,
    'rearFace'   : gold,
    'leftFace'   : orange,
    'rightFace'  : orange,
    'frontFace'  : garnet,
    'bottomFace' : eggplant,
}

Box(translate={ 'y' : -D }, **boxOptions) # top    # bottomFace=False
Box(translate={ 'y' :  D }, **boxOptions) # bottom # topFace=False
Box(translate={ 'z' :  D }, **boxOptions) # front  # rearFace=False
Box(translate={ 'z' : -D }, **boxOptions) # back   # frontFace
Box(translate={ 'x' :  D }, **boxOptions) # left   # rightFace=False
Box(translate={ 'x' : -D }, **boxOptions) # right  # leftFace=False

dotOptions = {

}

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'y': -D*2 },
    stroke=D, 
    color=gold)

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'y': D*2 },
    stroke=D, 
    color=gold)

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'x': -D*2 },
    stroke=D, 
    color=yellow)

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'x': D*2 },
    stroke=D, 
    color=garnet)

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'z': -D*2 },
    stroke=D, 
    color=orange)

Shape(
    addTo=model,
    path=[{ 'x': 0, 'y': 0 }],
    translate={ 'z': D*2 },
    stroke=D, 
    color=eggplant)

# dot.copy({
#   translate: { y: 2 },
#   color: gold,
# });

# dot.copy({
#   translate: { x: -2 },
#   color: yellow,
# });
# dot.copy({
#   translate: { x: 2 },
#   color: garnet,
# });
# dot.copy({
#   translate: { z: -2 },
#   color: orange,
# });
# dot.copy({
#   translate: { z: 2 },
#   color: eggplant,
# });

I.showInterface()
I.updateRenderGraph()
