# Dictionary storing the decimal values of Roman numerals
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_decimal(roman_numeral):
    """
    Function to convert a Roman numeral into its decimal value.
    Example: XIV -> 14
    """
    
    total = 0  # Variable to store the final result

    # Loop through the Roman numeral except the last character
    for i in range(len(roman_numeral) - 1):
        current = roman_numeral[i]
        next_value = roman_numeral[i + 1]

        # If the current value is smaller than the next value, subtract it
        if roman_values[current] < roman_values[next_value]:
            total -= roman_values[current]
        else:
            # Otherwise add it
            total += roman_values[current]

    # Add the value of the last numeral
    total += roman_values[roman_numeral[-1]]

    return total


# Take input from the user
roman_input = input("Enter a Roman Numeral: ").upper()

# Convert and display result
result = roman_to_decimal(roman_input)
print("The decimal value is:", result)