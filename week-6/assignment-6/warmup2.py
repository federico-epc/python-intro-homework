
def celsius_to_fahrenheit(c):    # Function to convert celcius to fahrenheit
    return (c * 9/5) + 32	


def fahrenheit_to_celsius(f):	 # Function to convert fahrenheit to celcius
    return 5 * (f - 32) / 9

print(f"0 °C = {celsius_to_fahrenheit(0):.1f} °F")  # Call the first function and print its result

print(f"37.5 °C = {celsius_to_fahrenheit(37.5):.1f} °F")


print(f"70 °F = {fahrenheit_to_celsius(70):.1f} °C")	# Call the second function and print its result
