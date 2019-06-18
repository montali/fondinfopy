import math

def sphere_density (radius, mass):
    volume=(4/3)*math.pi*(radius**3)
    return (mass/volume)
