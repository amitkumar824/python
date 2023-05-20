#python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("{:.2f} Celsius is equivalent to {:.2f} Fahrenheit".format(celsius, fahrenheit))
