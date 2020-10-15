weight = float(input('Enter the weight value in kg: '))
height = float(input('Enter the height value in meters: '))
bmi = weight / (height**2)

if bmi < 18.5:
    print('Under weight')
elif 18.5 <= bmi < 25:
    print('Normal weight')
elif bmi >= 25:
    print('Overweight')
