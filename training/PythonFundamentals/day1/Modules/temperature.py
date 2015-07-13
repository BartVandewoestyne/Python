def c2k(temperature):
    """Convert Celsius to Kelvin"""
    return temperature + 273.15


def k2c(temperature):
    """Convert Kelvin to Celsius"""
    return temperature - 273.15


def c2f(temperature):
    """Convert Celsius to Fahrenheit"""
    return (temperature * 9.0/5) + 32


def f2c(temperature):
    """Convert Fahrenheit to Celsius"""
    return (temperature - 32.0) * 5/9


def f2k(temperature):
    """Convert Fahrenheit to Kelvin"""
    return c2k(f2c(temperature))


def k2f(temperature):
    """Convert Kelvin to Fahrenheit"""
    return c2f(k2c(temperature))
