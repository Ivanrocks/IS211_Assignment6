def convertCelsiusToKelvin(celsius):
    """Converts Celsius to Kelvin.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Kelvin.
    """
    kelvins = (celsius + 273.15)

    return round(kelvins, 2)


def convertCelsiusToFahrenheit(celsius):
    """Converts Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    fahrenheit = (celsius * (9 / 5) + 32)

    return round(fahrenheit, 2)


def convertFahrenheitToCelsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius, 2)

def convertFahrenheitToKelvin(fahrenheit):
        """Converts Fahrenheit to Kelvin.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Kelvin.
    """
        celsius = (fahrenheit - 32) * (5 / 9)
        kelvin = celsius + 273.15
        return round(kelvin, 2)

def convertKelvinToFahrenheit(kelvin):
        """Converts Kelvin to Fahrenheit.

    Args:
        kelvin (float): The temperature in Kelvin.

    Returns:
        float: The temperature in Fahrenheit.
    """
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9 / 5) + 32
        return round(fahrenheit, 2)

def convertKelvinToCelsius(kelvin):
        """Converts Kelvin to Celsius.

    Args:
        kelvin (float): The temperature in Kelvin.

    Returns:
        float: The temperature in Celsius.
    """
        celsius = kelvin - 273.15
        return round(celsius, 2)

