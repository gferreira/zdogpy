'''Cylinder composite shape'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)
import zDogPy.pathCommand
reload(zDogPy.pathCommand)
import zDogPy.shape
reload(zDogPy.shape)
import zDogPy.group
reload(zDogPy.group)
import zDogPy.ellipse
reload(zDogPy.ellipse)

from zDogPy.boilerplate import TAU
from zDogPy.pathCommand import PathCommand
from zDogPy.shape import Shape
from zDogPy.group import Group
from zDogPy.ellipse import Ellipse

# -------------
# CylinderGroup
# -------------

class CylinderGroup(Group):

    color = '#333'
    updateSort = True

    # frontBase =
    # rearBase  =

    def __init__(self, **kwargs):
        Group.__init__(self, **kwargs)
        self.pathCommands = [
            PathCommand('move', [{}], None),
            PathCommand('line', [{}], None),
        ]

    def __repr__(self):
        return '<zDogPy CylinderGroup>'

    def render(self, ctx, renderer):
        self.renderCylinderSurface(ctx, renderer)
        Group.render(self, ctx, renderer)

    def renderCylinderSurface(self, ctx, renderer):
        if not self.visible:
            return

        # render cylinder surface
        frontBase   = self.frontBase
        rearBase    = self.rearBase
        scale       = frontBase.renderNormal.magnitude()
        strokeWidth = frontBase.diameter * scale + frontBase.getLineWidth()

        # set path command render points
        self.pathCommands[0].renderPoints[0].set(frontBase.renderOrigin)
        self.pathCommands[1].renderPoints[0].set(rearBase.renderOrigin)

        renderer.stroke(True, self.color, strokeWidth, lineCap='butt', lineJoin='miter')
        renderer.renderPath(self.pathCommands)
        renderer.end()

    def copyGraph(self):
        # prevent double-creation in parent.copyGraph()
        # only create in Cylinder.create()
        pass

# ---------------
# CylinderEllipse
# ---------------

class CylinderEllipse(Ellipse):

    def copyGraph(self):
        pass

# --------
# Cylinder
# --------

class Cylinder(Shape):

    def __init__(self, diameter=1, length=1, frontFace=True, backFace=True, fill=True, **kwargs):

        Shape.__init__(self, **kwargs)

        self.diameter  = diameter
        self.length    = length
        self.frontFace = frontFace
        self.backFace  = backFace
        self.fill      = fill

        self.group = CylinderGroup(addTo=self) # visible=self.visible, color=self.color

        baseZ     = self.length / 2
        baseColor = self.backface # if self.backface else True

        groupOptions = {
            'addTo'    : self.group,
            'diameter' : self.diameter,
            'color'    : self.color,
            'stroke'   : self.stroke,
            'fill'     : self.fill,
            'visible'  : self.visible
        }

        # front outside base
        self.group.frontBase = Ellipse(
            translate={ 'z': baseZ },
            rotate={ 'y': TAU / 2 },
            backface=self.frontFace, # || baseColor,
            **groupOptions)

        # back outside base
        self.group.rearBase = Ellipse(
            translate={ 'z': -baseZ },
            rotate={ 'y': 0 },
            backface=baseColor,
            **groupOptions)

    def __repr__(self):
        return f'<zDogPy Cylinder {self.diameter} {self.length}>'

    def render(self, ctx, renderer):
        # Cylinder shape does not render anything
        pass

    # --------------------
    # set child properties
    # --------------------

    childProperties = [ 'stroke', 'fill', 'color', 'visible' ]

    # for attr in childProperties:
        # use proxy property for custom getter & setter
        # _prop = '_' + attr

    # def _get(self, attr):
    #     prop = '_' + attr
    #     return getattr(self, prop)

    # def _set(self, attr, value):
    #     prop = '_' + attr
    #     setattr(self, prop, value)
    #     # set attr on children
    #     if self.frontBase:
    #         self.frontBase[attr] = value
    #         self.rearBase[attr]  = value
    #         self.group[attr]     = value

    ## TODO child property setter for backface, frontBaseColor, & rearBaseColor
