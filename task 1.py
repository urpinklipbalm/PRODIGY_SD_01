def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9 / 5) - 459.67


def main():
    print("\nWelcome to the Temperature Conversion Program!")
    print("============================================")

    # Get temperature value from the user
    temp_value = float(input("Please enter the temperature value you want to convert: "))

    # Get the original unit of measurement from the user
    print("Please enter the original unit of measurement:")
    print("C for Celsius")
    print("F for Fahrenheit")
    print("K for Kelvin")
    original_unit = input("Your choice (C/F/K): ").strip().upper()

    if original_unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temp_value)
        kelvin = celsius_to_kelvin(temp_value)
        print(f"\n{temp_value} degrees Celsius is equivalent to:")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
    elif original_unit == 'F':
        celsius = fahrenheit_to_celsius(temp_value)
        kelvin = fahrenheit_to_kelvin(temp_value)
        print(f"\n{temp_value} degrees Fahrenheit is equivalent to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{kelvin:.2f} Kelvin")
    elif original_unit == 'K':
        celsius = kelvin_to_celsius(temp_value)
        fahrenheit = kelvin_to_fahrenheit(temp_value)
        print(f"\n{temp_value} Kelvin is equivalent to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
    else:
        print("\nInvalid unit of measurement. Please enter C, F, or K.")

    print("\nthank u :)")


if __name__ == "__main__":
    main()
