### BUGGY !!!

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.illustration
reload(zDogPy.illustration)
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.hemisphere
reload(zDogPy.hemisphere)

from zDogPy.boilerplate import TAU
from zDogPy.illustration import Illustration
from zDogPy.anchor import Anchor
from zDogPy.rect import Rect
from zDogPy.ellipse import Ellipse
from zDogPy.hemisphere import Hemisphere
from zDogPy.cylinder import Cylinder

yellow = '#ED0'
gold   = '#EA0'
orange = '#E62'
garnet = '#C25'

I = Illustration()
I.setSize(400, 400)

burger = Anchor(addTo=I,
    translate={ 'y': 0 },
    rotate={ 'x' : TAU / 4 }
)

topBun = Hemisphere(
    addTo=burger,
    diameter=96,
    translate={ 'z' : 0 },
    stroke=14,
    fill=True,
    color=orange)

cheese = Rect(
    addTo=burger,
    width=92,
    height=92,
    translate={ 'z' : 25 },
    stroke=16,
    color=yellow,
    fill=True)

patty = Ellipse(
    addTo=burger,
    diameter=96,
    stroke=32,
    translate={ 'z' : 53 },
    color=garnet,
    fill=True)

bottomBun = Cylinder(
    addTo=burger,
    diameter=topBun.diameter,
    length=16,
    translate={ 'z': 90 },
    stroke=topBun.stroke,
    color=topBun.color)

# // var seedAnchor = new Zdog.Anchor({
# //   addTo: burger,
# //   translate: topBun.translate,
# // });
# var seedAnchor = new Zdog.Anchor({
#   addTo: topBun,
# });

# var seedZ = ( topBun.diameter + topBun.stroke ) / 2 + 1;
# // seed
# new Zdog.Shape({
#   addTo: seedAnchor,
#   path: [ { y: -3 }, { y: 3 } ],
#   translate: { z: seedZ },
#   stroke: 8,
#   color: gold,
# });

# seedAnchor.copyGraph({
#   rotate: { x: 0.6 },
# });
# seedAnchor.copyGraph({
#   rotate: { x: -0.6 },
# });
# seedAnchor.copyGraph({
#   rotate: { y: -0.5 },
# });
# seedAnchor.copyGraph({
#   rotate: { y: 0.5 },
# });





I.showInterface()
I.updateRenderGraph()

