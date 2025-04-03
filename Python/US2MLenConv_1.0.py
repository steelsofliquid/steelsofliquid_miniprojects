# python 3.12.2

from time import *

print("Customary to Metric Length Convertor 1.0")
print("by steelsofliquid")

startunit = ''
endunit = ''

value1 = float()
value2 = float()
result = float()

# was gonna use functions here but nevermind

sleep(1)

startunit = input('Starting unit: ')
endunit = input('Unit to convert to: ')

if startunit == 'in':
    if endunit == 'cm': # you're gonna have to use the abbreviated terms because it acts up when i use or... at least for now.
        print("Inches -> Centimetres")
        value1 = float(input('How many inches? '))
        result = value1 * 2.54

        sleep(0.2)

        print(value1, " inches is equal to ", result, " centimetres.", sep='')
    elif endunit == 'mm':
        print("Inches -> Millimetres")
        value1 = float(input('How many inches? '))
        result = value1 * 25.4

        sleep(0.2)

        print(value1, " inches is equal to ", result, " millimetres.", sep='')
    elif endunit == 'm':
        print("Inches -> Metres")
        value1 = float(input('How many inches? '))
        result = value1 / 39.37

        sleep(0.2)

        print(value1, " inches is equal to ", result, " metres.", sep='')
    elif endunit == 'km':
        print("Inches -> Kilometres")
        value1 = float(input('How many inches? '))
        result = value1 / 39370

        sleep(0.2)

        print(value1, " inches is equal to ", result, " kilometres.", sep='')
    else:
        print("While other units may exist in the metric system, they go beyond the scope of this brief project.")

elif startunit == 'ft':
    if endunit == 'cm':
        print("Feet -> Centimetres")
        value1 = float(input('How many feet? '))
        result = value1 * 30.48

        sleep(0.2)

        print(value1, " feet is equal to ", result, " centimetres.", sep='')
    elif endunit == 'mm':
        print("Feet -> Millimetres")
        value1 = float(input('How many feet? '))
        result = value1 * 304.8

        sleep(0.2)

        print(value1, " feet is equal to ", result, " millimetres.", sep='')
    elif endunit == 'm':
        print("Feet -> Metres")
        value1 = float(input('How many feet? '))
        result = value1 / 3.281

        sleep(0.2)

        print(value1, " feet is approximately equal to ", result, " metres.", sep='')
    elif endunit == 'km':
        print("Feet -> Kilometres")
        value1 = float(input('How many feet? '))
        result = value1 / 3281

        sleep(0.2)

        print(value1, " feet is approximately equal to ", result, " kilometres.", sep='')
    else:
        print("While other units may exist in the metric system, they go beyond the scope of this brief project.")

elif startunit == 'yd':
    if endunit == 'cm':
        print("Yards -> Centimetres")
        value1 = float(input('How many yards? '))
        result = value1 * 91.44

        sleep(0.2)

        print(value1, " yards is equal to ", result, " centimetres.", sep='')
    elif endunit == 'mm':
        print("Yards -> Millimetres")
        value1 = float(input('How many yards? '))
        result = value1 * 914.4

        sleep(0.2)

        print(value1, " yards is equal to ", result, " millimetres.", sep='')
    elif endunit == 'm':
        print("Yards -> Metres")
        value1 = float(input('How many yards? '))
        result = value1 / 1.094

        sleep(0.2)

        print(value1, " yards is approximately equal to ", result, " metres.", sep='')
    elif endunit == 'km':
        print("Yards -> Kilometres")
        value1 = float(input('How many yards? '))
        result = value1 / 1094

        sleep(0.2)

        print(value1, " yards is approximately equal to ", result, " kilometres.", sep='')
    else:
        print("While other units may exist in the metric system, they go beyond the scope of this brief project.")

elif startunit == 'mi':
    if endunit == 'cm':
        print("Miles -> Centimetres")
        print("Too large of a difference to calculate >_<") # scientific notations scare me /j
    elif endunit == 'mm':
        print("Miles -> Millimetres")
        print("Too large of a difference to calculate >_<")
    elif endunit == 'm':
        print("Miles -> Metres")
        value1 = float(input('How many miles? '))
        result = value1 * 1609

        sleep(0.2)

        print(value1, " miles is approximately equal to ", result, " metres.", sep='')
    elif endunit == 'km':
        print("Miles -> Kilometres")
        value1 = float(input('How many miles? '))
        result = value1 * 1.609

        sleep(0.2)

        print(value1, " miles is approximately equal to ", result, " kilometres.", sep='')
    else:
        print("While other units may exist in the metric system, they go beyond the scope of this brief project.")

else:
    print("That\'s not a valid unit. For context, this is only from customary to metric.")


# holy crap this took hours
