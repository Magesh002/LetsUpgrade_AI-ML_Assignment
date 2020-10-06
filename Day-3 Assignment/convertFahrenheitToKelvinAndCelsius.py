def convertCelsiusToKelvin(celsiusValue):
    return celsiusValue + 237.15


def convertFahrenheitToCelsiusAndKelvin(fahrenheitValue):
    celsius = (fahrenheitValue - 32)*(5/9)
    kelvin = convertCelsiusToKelvin(celsiusValue=celsius)
    return celsius, kelvin


f = float(input("Enter the fahrenheit value: "))
c, k = convertFahrenheitToCelsiusAndKelvin(fahrenheitValue=f)

print("The celsius value is:", c, "and the kelvin value is:", k)