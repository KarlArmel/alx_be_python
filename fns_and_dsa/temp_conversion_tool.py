FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
OFFSET = 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, OFFSET
    celsius = (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, OFFSET
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return fahrenheit

def main():
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
