def convert_temperature(value, unit):
    if unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        return (value - 32) * 5/9
    else:
        return None  # Invalid unit

# Get user input
temperature_input = float(input("Enter the temperature value: "))
unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert the temperature
converted_temp = convert_temperature(temperature_input, unit_input)

# Display the result
if converted_temp is not None:
    if unit_input.upper() == 'C':
        print(f"{temperature_input}°C is equal to {converted_temp:.2f}°F")
    elif unit_input.upper() == 'F':
        print(f"{temperature_input}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")