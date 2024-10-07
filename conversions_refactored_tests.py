import conversions_refactored

import unittest

class TestTemperatureConversion(unittest.TestCase):
    """
    Known_values: stores the know values for converting from and to
    Tuple organization:
    known_values[0]: Units to convert from fromUnit
    known_values[1]: Units to convert to toUnit
    known_values[2]: Tuple with know values. First value is the unit to convert. Second value is the expected result
    known_values[2][0]: unit to convert
    known_values[2][0] expected value
    """
    known_values = [
        ("celsius", "kelvin", [
            (0, 273.15), (-40, 233.15), (100, 373.15), (-273.15, 0)
        ]),
        ("celsius", "fahrenheit", [
            (0, 32), (100, 212), (-40, -40), (-273.15, -459.67)
        ]),
        ("fahrenheit", "celsius", [
            (32, 0), (212, 100), (-40, -40), (-459.67, -273.15)
        ]),
        ("fahrenheit", "kelvin", [
            (32, 273.15), (212, 373.15), (-40, 233.15), (-459.67, 0)
        ]),
        ("kelvin", "celsius", [
            (273.15, 0), (233.15, -40), (373.15, 100), (0, -273.15)
        ]),
        ("kelvin", "fahrenheit", [(
            273.15, 32), (233.15, -40), (373.15, 212), (0, -459.67)
        ]),
        ("miles", "yards", [
            (1, 1760), (2, 3520), (0.5, 880), (10, 17600)
        ]),
        ("miles", "meters", [
            (1, 1609.34), (2, 3218.68), (0.5, 804.67), (10, 16093.4)
        ]),
        ("yards", "miles", [
            (1760, 1), (3520, 2), (880, 0.5), (17600, 10)
        ]),
        ("yards", "meters", [
            (1, 0.91), (2, 1.83), (0.5, 0.46), (10, 9.14)
        ]),
        ("meters", "miles", [
            (1609.34, 1), (3218.68, 2), (804.67, 0.5), (16093.4, 10)
        ]),
        ("meters", "yards", [
            (0.91, 1), (1.83, 2), (0.4572, 0.5), (9.14, 10)
        ])
    ]


    def test_conversions_refactored(self):
        for test in self.known_values:
            print("Testing {0} to {1}.".format(test[0],test[1]))
            for case in test[2]:
                print("Checking {0} {1} to {2} {3}.".format(case[0],test[0],case[1], test[1]))
                result = conversions_refactored.convert(test[0], test[1], case[0])
                self.assertEqual(case[1],result)
            print("\n")

    def test_bad_fromUnit_input(self):
        print("Testing bad input fromUnit")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            self.assertRaises(conversions_refactored.convert("Meteor","",0))

    def test_bad_toUnit_input(self):
        print("Testing bad input toUnit")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            self.assertRaises(conversions_refactored.convert("Meter","Meteor",0))


    def test_converting_incompatible_units(self):
        print("Testing bad input toUnit")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            self.assertRaises(conversions_refactored.convert("Meter","kelvin",0))

    def test_bad_value_input(self):
        print("Testing bad input value")
        with self.assertRaises(conversions_refactored.NotANumber):
            self.assertRaises(conversions_refactored.convert("Meter","Meteor","0p"))

if __name__ == '__main__':
    unittest.main()