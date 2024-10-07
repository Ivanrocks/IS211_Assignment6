# IS211_Assignment6
## Introduction
This Python module provides a versatile function for converting values between various temperature and distance units. It supports conversions among Celsius, Fahrenheit, Kelvin, miles, yards, and meters.

## Usage
```python
import conversions_refactored

# Convert temperature
result = conversions_refactored.convert("celsius", "fahrenheit", 32)
print(result)  # Output: 89.6

# Convert distance
result = conversions_refactored.convert("miles", "yards", 1)
print(result)  # Output: 1760.0

# Invalid conversion
try:
    result = conversions_refactored.convert("meters", "pounds", 5)
except conversions_refactored.ConversionNotPossible:
    print("Conversion not possible")
```

## Function Description
convert(fromUnit, toUnit, value)

* fromUnit: The unit to convert from (e.g., "celsius", "miles").
* toUnit: The unit to convert to (e.g., "fahrenheit", "yards").
* value: The value to be converted.

Returns: The converted value as a float, rounded to two decimal places.

## Raises
* ConversionNotPossible: If the conversion between the specified units is not supported.
* NotANumber: If the value argument is not a valid number.

## Supported Conversions
Supported Conversions

From Unit | To Units
--- | ---
Celsius |	Fahrenheit, Kelvin
Fahrenheit	| Celsius, Kelvin
Kelvin	| Celsius, Fahrenheit
Miles	| Yards, Meters
Yards	| Miles, Meters
Meters	| Miles, Yards

## Additional Notes
* The function is case-insensitive, so you can use uppercase or lowercase for unit names.
* The function handles invalid conversions gracefully by raising a ConversionNotPossible exception.
* The function ensures that converting a value from a unit to itself returns the same value.
### Contributor:
Ivan Martinez
