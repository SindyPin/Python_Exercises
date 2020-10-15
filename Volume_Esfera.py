# Sphere Calculation

import math

radius_sphere = float(input('Enter the radius of the sphere: '))
sphere_volume = (4/3) * math.pi * (radius_sphere**3)
print('The volume of the sphere is ', round(sphere_volume, 2))