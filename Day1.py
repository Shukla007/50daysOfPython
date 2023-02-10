def convert_base(num_as_string, from_base, to_base):
    if isinstance(num_as_string, str):
        # Convert the number from string to int with the specified base
        num = int(num_as_string, from_base)
    else:
        # The input is already an int, so just assign it to num
        num = num_as_string

    # Check if the to_base is 10, then return the num as is
    if to_base == 10:
        return num
    else:
        # Use the built-in method to convert the number to the desired base
        return format(num, f'0{to_base}b')[2:]

print("Binary of 10:", convert_base(10, 10, 2))
print("Octal of 10:", convert_base(10, 10, 8))
print("Hexadecimal of 10:", convert_base(10, 10, 16))
print("Custom base of 11 (3):", convert_base("1011", 2, 3))
