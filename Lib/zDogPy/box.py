'''Box composite shape'''

from importlib import reload
import zDogPy.anchor
reload(zDogPy.anchor)
import zDogPy.shape
reload(zDogPy.shape)
import zDogPy.rect
reload(zDogPy.rect)

from zDogPy.anchor import Anchor
from zDogPy.shape import Shape
from zDogPy.rect import Rect
from zDogPy.boilerplate import TAU

# -------
# BoxRect
# -------

class BoxRect(Rect):

    def copyGraph(self):
        pass

# ---
# Box
# ---

class Box(Anchor):

    frontFace  = None
    rearFace   = None
    leftFace   = None
    rightFace  = None
    topFace    = None
    bottomFace = None

    def __init__(self, width=1, height=1, depth=1, stroke=1, fill=True, color=True, frontFace=True, rearFace=True, leftFace=True, rightFace=True, topFace=True, bottomFace=True, **kwargs):

        self.width  = width
        self.height = height
        self.depth  = depth
        self.stroke = stroke
        self.fill   = fill
        self.color  = color

        self.frontFace  = frontFace
        self.rearFace   = rearFace
        self.leftFace   = leftFace
        self.rightFace  = rightFace
        self.topFace    = topFace
        self.bottomFace = bottomFace

        Anchor.__init__(self, **kwargs)

        self.updatePath()

    def updatePath(self):
        self.setFace('frontFace', {
            'width'     : self.width,
            'height'    : self.height,
            'translate' : { 'z': self.depth / 2 },
        })
        self.setFace('rearFace', {
            'width'     : self.width,
            'height'    : self.height,
            'translate' : { 'z': -self.depth / 2 },
        })
        self.setFace('leftFace', {
            'width'     : self.depth,
            'height'    : self.height,
            'translate' : { 'x': -self.width / 2 },
            'rotate'    : { 'y': -TAU / 4 },
        })
        self.setFace('rightFace', {
            'width'     : self.depth,
            'height'    : self.height,
            'translate' : { 'x': self.width / 2 },
            'rotate'    : { 'y': TAU / 4 },
        })
        self.setFace('topFace', {
            'width'     : self.width,
            'height'    : self.depth,
            'translate' : { 'y': -self.height / 2 },
            'rotate'    : { 'x': -TAU / 4 },
        })
        self.setFace('bottomFace', {
            'width'     : self.width,
            'height'    : self.depth,
            'translate' : { 'y': self.height / 2 },
            'rotate'    : { 'x': -TAU / 4 },
        })

    def setFace(self, faceName, options):

        attr = getattr(self, faceName)
        rectProperty = faceName + 'Rect'

        # remove if False
        if not attr:
            # self.removeChild(rectProperty)
            return

        rect = BoxRect(**options)
        # rect.setOptions(options)

        # color: typeof property == 'string' ? property : this.color,
        rect.stroke = self.stroke
        rect.fill   = self.fill
        rect.color  = self.color
        # rect.backface   = self.backface
        # rect.front      = self.front
        # rect.visible    = self.visible

        # # rect.color    = self.color,
        # # rect.stroke   = self.stroke
        # # rect.fill     = self.fill
        # # rect.backface = self.backface
        # # rect.front    = self.front
        # # rect.visible  = self.visible

        rect.updatePath()
        self.addChild(rect)

