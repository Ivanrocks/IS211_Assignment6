import conversions
import unittest

from IS211_Assignment6.conversions_refactored import convert


class KnownValues(unittest.TestCase):
    """
    known_values is a pair of known farenheit-celcius conversion values

    """
    known_values_Celsius_Fahrenheit = (
        (-40, -40),
        (-10, 14),
        (0, 32),
        (90, 194),
        (150, 302)
    )
    known_values_Celsius_Kelvin = (
    (-40, 233.15),
    (-10, 263.15),
    (0, 273.15),
    (10, 283.15),
    (150, 423.15)
)
    known_values_Fahrenheit_Kelvin = (
        (32.0, 273.15),
        (80.33, 300),
        (212.0, 373.15),
        (260.33, 400),
        (350.33, 450)
    )


    def test_convertCelsiusToFahrenheit(self):
        for celsius, fahrenheit in self.known_values_Celsius_Fahrenheit:
            print("Testing {0} Celsius to Fahrenheit. Expected result is : {1}".format(celsius,fahrenheit))
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit,result)

    def test_convertCelsiusToKelvin(self):
        for celsius, kelvin in self.known_values_Celsius_Kelvin:
            print("Testing {0} Celsius to Kelvin. Expected result is : {1}".format(celsius,kelvin))

            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin,result)
    def test_convertFahrenheitToCelsius(self):
        for celsius, fahrenheit in self.known_values_Celsius_Fahrenheit:
            print("Testing {0} Fahrenheits to Celsius. Expected result is {1}".format(fahrenheit, celsius))
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius,result)

    def test_convertFahrenheitToKelvin(self):
        for fahrenheit, kelvin in self.known_values_Fahrenheit_Kelvin:
            print("Testing {0} Fahrenheits to Celsius. Expected result is {1}".format(fahrenheit, kelvin))
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin,result)

    def test_convertKelvinToFahrenheit(self):
        for fahrenheit, kelvin in self.known_values_Fahrenheit_Kelvin:
            print("Testing {0} Fahrenheits to Celsius. Expected result is {1}".format(kelvin, fahrenheit))
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit,result)

    def test_convertKelvinToCelsius(self):
        for celsius,kelvin in self.known_values_Celsius_Kelvin:
            print("Testing {0} Fahrenheits to Celsius. Expected result is {1}".format(kelvin, celsius))
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius,result)

if __name__ == '__main__':
    unittest.main()