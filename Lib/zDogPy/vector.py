'''Vector'''

from importlib import reload
import zDogPy.boilerplate
reload(zDogPy.boilerplate)

import math
from zDogPy.boilerplate import TAU, lerp

class Vector:

    x = 0
    y = 0
    z = 0

    def __init__(self, position=None, **kwargs):
        self.set(position, **kwargs)

    def __repr__(self):
        return f'<zDogPy Vector {self.x} {self.y} {self.z}>'

    def set(self, pos, **kwargs):

        if pos and hasattr(pos, 'x'):
            self.x = pos.x
        elif 'x' in kwargs:
            self.x = kwargs['x']
        elif pos:
            self.x = pos

        if pos and hasattr(pos, 'y'):
            self.y = pos.y
        elif 'y' in kwargs:
            self.y = kwargs['y']
        elif pos:
            self.y = pos

        if pos and hasattr(pos, 'z'):
            self.z = pos.z
        elif 'z' in kwargs:
            self.z = kwargs['z']
        elif pos:
            self.z = pos

        return self

    def write(self, **kwargs):
        # set coordinates without sanitizing
        # vec.write({ y: 2 }) only sets y coord
        if 'x' in kwargs:
            self.x = x
        if 'y' in kwargs:
            self.y = y
        if 'z' in kwargs:
            self.z = z
        return self

    def scale(self, scale):
        if not scale:
            return
        result = self.multiply(scale)
        self.x = result.x
        self.y = result.y
        self.z = result.z
        return self

    def translate(self, translation):
        if not translation:
            return
        result = self.add(translation)
        self.x = result.x
        self.y = result.y
        self.z = result.z
        return self

    def rotate(self, rotation):
        if rotation is None:
            return

        if isinstance(rotation, dict):
            rotation = Vector(**rotation)

        self.rotateZ(rotation.z)
        self.rotateY(rotation.y)
        self.rotateX(rotation.x)

        return self

    def rotateZ(self, angle):
        self.rotateProperty(self, angle, 'x', 'y')

    def rotateX(self, angle):
        self.rotateProperty(self, angle, 'y', 'z')

    def rotateY(self, angle):
        self.rotateProperty(self, angle, 'x', 'z')

    def rotateProperty(self, vec, angle, propA, propB):
        if not angle or angle % TAU == 0:
            return
        cos = math.cos(angle)
        sin = math.sin(angle)
        a = getattr(vec, propA)
        b = getattr(vec, propB)
        setattr(vec, propA, a * cos - b * sin)
        setattr(vec, propB, b * cos + a * sin)

    def add(self, pos):

        if pos is None:
            return

        if hasattr(pos, 'x'):
            self.x += pos.x
        else:
            # self.x += pos
            pass

        if hasattr(pos, 'y'):
            self.y += pos.y
        else:
            # self.y += pos
            pass

        if hasattr(pos, 'z'):
            self.z += pos.z
        else:
            # self.z += pos
            pass

        return self

    def subtract(self, pos):
        if pos is None:
            return # self

        self.x -= pos.x if isinstance(pos, Vector) else 0
        self.y -= pos.y if isinstance(pos, Vector) else 0
        self.z -= pos.z if isinstance(pos, Vector) else 0

        return self

    def multiply(self, pos):

        if pos is None:
            return

        if isinstance(pos, Vector):
            self.x *= pos.x
            self.y *= pos.y
            self.z *= pos.z

        elif isinstance(pos, float) or isinstance(pos, int):
            self.x *= pos
            self.y *= pos
            self.z *= pos

        else:
            self.x *= 1
            self.y *= 1
            self.z *= 1

        return self

    def transform(self, translation, rotation, scale):
        self.multiply(scale)
        self.rotate(rotation)
        self.add(translation)
        return self

    def lerp(self, pos, t):
        self.x = lerp(self.x, pos.x or 0, t)
        self.y = lerp(self.y, pos.y or 0, t)
        self.z = lerp(self.z, pos.z or 0, t)
        return self

    def magnitude(self):
        _sum = self.x * self.x + self.y * self.y + self.z * self.z
        return self.getMagnitudeSqrt(_sum)

    def getMagnitudeSqrt(self, sum_):
        # PERF: check if sum ~= 1 and skip sqrt
        if (abs(sum_ - 1) < 0.00000001):
            return 1
        return math.sqrt(sum_)

    def magnitude2d(self):
        _sum = self.x * self.x + self.y * self.y
        return self.getMagnitudeSqrt(_sum)

    def copy(self):
        return Vector(self)
