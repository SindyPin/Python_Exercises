# Calculate the distance between 2 points of an ordered pair from the plane
pointPx = float(input('Enter the X-value from the first ordinate pair: '))
pointPy = float(input('Enter the Y-value from the first ordinate pair: '))
pointQx = float(input('Enter the X-value from the second ordinate pair: '))
pointQy = float(input('Enter the Y-value from the second ordinate pair: '))
distance = ((pointQx - pointPx)**2 + (pointQy - pointPy)**2)**(1/2)
print('The distance between the two points from the plane is ', round(distance, 2))
