

def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    try:
        value = float(value)
    except:

        raise NotANumber

    allowedConversions = {
        "celsius": {
            "fahrenheit": lambda x: x *(9/5) + 32,
            "kelvin": lambda x: x + 273.15,
        },
        "fahrenheit": {
            "celsius": lambda x: (x - 32) * (5 / 9),
            "kelvin": lambda x: (x - 32) * (5 / 9) + 273.15

        },
        "kelvin": {
            "celsius": lambda x: x - 273.15,
            "fahrenheit": lambda x: (x - 273.15) * (9 / 5) + 32
        },
        "miles": {
            "yards": lambda x: x * 1760,
            "meters": lambda x: x * 1609.34
        },
        "yards": {
            "miles": lambda x: x / 1760,
            "meters": lambda x: x * 0.9144
        },
        "meters": {
            "miles": lambda x: x / 1609.34,
            "yards": lambda x: x / 0.9144
        }
    }
    #Requirement: Check that converting from incompatible units will raise a ConversionNotPossible exception
    if fromUnit == toUnit:
        return float(value)

    if fromUnit not in allowedConversions.keys() or toUnit not in allowedConversions[fromUnit].keys():
        raise ConversionNotPossible

    #Requirement: Check that converting from one unit to itself returns the same value for all units

    result = allowedConversions[fromUnit][toUnit](value)

    return float(round(result,2))

class ConversionNotPossible(Exception):
    pass

class NotANumber(Exception):
    pass

