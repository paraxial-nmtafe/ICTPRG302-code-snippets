def celsius_to_fahrenheit(temperature):
    return temperature * (9/5) + 32

def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5/9)

"""
    We have taught you if/else flows in class.  Here, I have not used the 'else'
    statement.  Consider why not, and whether or not it would be necessary.

    What conditional case is missing from this function?
"""
def temperature_converter(temp, unit):
    if unit == "F":
        return celsius_to_fahrenheit(temp)
    if unit == "C":
        return fahrenheit_to_celsius(temp)

print("Convert a temperature!")
try:
    temperature = float(input("What temperature would you like to convert? ").strip())
except ValueError:
    print("Input a number instead please.")
    exit(1)

unit = input("Which unit would you like to convert to, C or F? ").upper()

print("The converted temperature is:", temperature_converter(temperature, unit), unit)
