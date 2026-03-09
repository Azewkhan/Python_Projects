# Function to convert Fahrenheit to Celsius

def convert(temp):
    Fahrenheit = float(temp)
    Celcius = (Fahrenheit - 32) * 5/9
    return Celcius

Temp = input("Enter your Temperature in Fahrenheit: ")

result = convert(Temp)
print("Temperature in Celsius is:", result)

