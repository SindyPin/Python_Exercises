sideA = float(input('Enter the first side value of the triangle: '))
sideB = float(input('Enter the second side value of the triangle: '))
sideC = float(input('Enter the third side value of the triangle: '))

if (sideA < sideB + sideC and sideB < sideA + sideC and sideC < sideA + sideB ) and (sideA == sideB == sideC):
    print('The figure is an equilateral triangle (all sides are equal)')
elif (sideA < sideB + sideC and sideB < sideA + sideC and sideC < sideA + sideB) and (sideA != sideB != sideC):
    print('The figure is an scalene triangle (all sides are different)')
elif (sideA < sideB + sideC and sideB < sideA + sideC and sideC < sideA + sideB) and ((sideA == sideB) or (sideA == sideC) or (sideB == sideC)):
    print('The figure is an isosceles triangle (only two sides are equal)')
else:
    print('The figure is not a triangle')
