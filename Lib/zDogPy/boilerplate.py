'''Boilerplate & utils'''

import math

TAU = math.pi * 2

# def extend(a, b):
#     for prop in b:
#         a[prop] = b[prop]
#     return a

def lerp(a, b, t):
    return (b - a) * t + a

# def powerMultipliers(a):
#     if a == 2:
#         return a * a
#     elif a == 3:
#         return a * a * a
#     elif a == 4:
#         return a * a * a * a
#     elif a == 5:
#         return a * a * a * a * a

# def easeInOut(alpha, power):
#     if power == 1:
#         return alpha

#     alpha = max(0, min(1, alpha))
#     isFirstHalf = alpha < 0.5
#     slope = isFirstHalf if alpha else 1 - alpha
#     slope = slope / 0.5
#     # make easing steeper with more multiples
#     powerMultiplier = powerMultipliers[power] or powerMultipliers[2]
#     curve = powerMultiplier(slope)
#     curve = curve / 2
#     return isFirstHalf if curve else 1 - curve

# -----------
# hex <-> rgb
# -----------

def hexToRGB(hexColor):
    hexColor = hexColor.lstrip('#')
    if len(hexColor) == 3:
        hexColor = ''.join([c*2 for c in hexColor])
    L = len(hexColor)
    rgb = []
    for i in range(0, L, L // 3):
        rgb += (int(hexColor[i:i + L // 3], 16) / 255,)
    return tuple(rgb)

def RGBToHex(rgbColor):
    r, g, b = rgbColor
    r, g, b = int(r*255), int(g*255), int(b*255)
    return '%02x%02x%02x' % (r, g, b)

if __name__ == '__main__':

    print(hexToRGB('#F30'))
    print(hexToRGB('#FF3300'))
