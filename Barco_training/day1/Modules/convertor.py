import argparse

# TODO: shouldn't the program under section 3.1.4 on page 7 be convertor.py instead of temperature.py?

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c2f", dest="degrees_celsius", type=float, help="Celsius to Fahrenheit")
    parser.add_argument("-c2k", dest="degrees_celsius", type=float, help="Celsius to Kelvin")
    parser.add_argument("-f2c", dest="degrees_fahrenheit", type=float, help="Fahrenheit to Celsius")
    parser.add_argument("-k2c", dest="degrees_kelvin", type=float, help="Kelvin to Celsius")
    parser.add_argument("-f2k", dest="degrees_fahrenheit", type=float, help="Fahrenheit to Kelvin")
    parser.add_argument("-k2f", dest="degrees_kelvin", type=float, help="Kelvin to Fahrenheit")
    args = parser.parse_args()

    print([arg for arg in vars(args)])
    # TODO: how to proceed from here???
