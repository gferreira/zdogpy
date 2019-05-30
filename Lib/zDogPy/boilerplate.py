'''Boilerplate & utils'''

import math

TAU = math.pi * 2

def extend(a, b):
    for prop in b:
        a[prop] = b[prop]
    return a

def lerp(a, b, t):
    return (b - a) * t + a

def powerMultipliers(a):
    if a == 2:
        return a * a
    elif a == 3:
        return a * a * a
    elif a == 4:
        return a * a * a * a
    elif a == 5:
        return a * a * a * a * a

def easeInOut(alpha, power):
    if power == 1:
        return alpha

    alpha = max(0, min(1, alpha))
    isFirstHalf = alpha < 0.5
    slope = isFirstHalf if alpha else 1 - alpha
    slope = slope / 0.5
    # make easing steeper with more multiples
    powerMultiplier = powerMultipliers[power] or powerMultipliers[2]
    curve = powerMultiplier(slope)
    curve = curve / 2
    return isFirstHalf if curve else 1 - curve
