def convert_octal_to_binary(num1):
    if not all(char in '01234567' for char in num1):
        print("Invalid input.")
        return
    
    binary = ''
    for char in num1:
        octal_digit = int(char)
        
        digit = f'{octal_digit:03b}'
        binary += digit
    
    binary = binary.lstrip('0')
    
    #print(f'Entered number in binary is: [{binary}]')
    return binary
    
def convert_decimal_to_binary(num1):
    if num1 == 0:
        print("Entered number in binary is: [0]")
        return
    
    binary = ''
    
    while num1 > 0:
        binary = str(num1 % 2) + binary
        num1 = num1 // 2
    
    #print(f'Entered number in binary is: [{binary}]')
    return binary

def convert_hex_to_binary(num1):
    
    if not all(char in '0123456789ABCDEFabcdef' for char in num1):
        print("Invalid input.")
        return
    
    binary = ''
    for char in num1:
        hex_digit = int(char, 16) 

        digit = f'{hex_digit:04b}'
        binary += digit
    
    binary = binary.lstrip('0')
    
    #print(f'Entered number in binary is: [{binary}]')
    return binary
    
def convert_binary_to_decimal(num1):

    if not all(char in '01' for char in num1):
        print("Invalid input.")


    decimal = 0
    x = len(num1) - 1
    
    for char in num1:
        if char == '1':
            decimal += 2 ** x
        x -= 1
    
    #print(f'Entered number in decimal is: [{decimal}]')
    return decimal
    
def convert_decimal_to_octal(num1):
    if num1 == 0:
        print("Entered number in octal is: [0]")
    
    else: 
        num2 = []
        while num1 > 0:
            res = num1 % 8
            num2.append(str(res))
            num1 = num1 // 8
    
        num2.reverse()

        octal = ''.join(digit for digit in num2)
    
        #print(f'Entered number in octal is: [{octal}]')
        return octal

def convert_decimal_to_hexadecimal(num1):
    if num1 == 0:
        print("Entered number in hexadecimal is: [0]")
    
    else:
        hex_digits = '0123456789ABCDEF'
        num2 = []
        while num1 > 0:
            res = num1 % 16
            num2.append(hex_digits[res])
            num1 = num1 // 16
    
        num2.reverse()

        hex = ''.join(digit for digit in num2)
    
        #print(f'Entered number in hexadecimal is: [{hex}]')
        return hex

def accept():
    num1 = int(input("Enter input base: "))
    
    if num1 not in (2, 8, 10, 16):
        print("Invalid input base.")
        return None
    else:
        return num1

def output():
    
    num1 = int(input("Enter output base: "))  
    if num1 not in (2, 8, 10, 16):
        print("Invalid output base.")
        return None
    else:
        return num1
    
###########################################

print("Welcome to Base converter [v0.6.1]")

print("\n[binary = 2] \n[octal = 8] \n[decimal = 10] \n[hexadecimal = 16] \n")

user_in = accept()
if user_in:
    
    user_val = input("Enter value to be converted: ")
    
    user_out = output()
    print()

    if user_out:
        match (user_in, user_out):
            case (2, 2): #bin to bin
                print("Binary to binary conversion really?")
                print(f'Input value in Binary is [{user_val}]')
            case (2, 8): #bin to oct
                x = convert_binary_to_decimal(user_val)
                res = convert_decimal_to_octal(x)
                print(f'Input value in Octal is [{res}]')
            case (2, 10): #bin to dec
                res = convert_binary_to_decimal(user_val)
                print(f'Input value in Decimal is [{res}]')
            case (2, 16): #bin to hex
                x = convert_binary_to_decimal(user_val)
                res = convert_decimal_to_hexadecimal(x)
                print(f'Input value in Hexadecimal is [{res}]')
            case (8, 2): #oct to bin
                res = convert_octal_to_binary(user_val)
                print(f'Input value in Binary is [{res}]')
            case (8, 8): #oct to oct
                print("Octal to octal conversion really?")
                print(f'Input value in Octal is [{user_val}]')
            case (8, 10): #oct to dec
                x = convert_octal_to_binary(user_val)
                res = convert_binary_to_decimal(x)
                print(f'Input value in Decimal is [{res}]')
            case (8, 16): #oct to hex
                x = convert_octal_to_binary(user_val)
                y = convert_binary_to_decimal(x)
                res = convert_decimal_to_hexadecimal(y)
                print(f'Input value in Hexadecimal is [{res}]')
            case (10, 2): #dec to bin
                res = convert_decimal_to_binary(int(user_val))
                print(f'Input value in Binary is [{res}]')
            case (10, 8): #dec to oct
                res = convert_decimal_to_octal(int(user_val))
                print(f'Input value in Octal is [{res}]')
            case (10, 10): #dec to dec
                print("Decimal to Decimal conversion really?")
                print(f'Input value in Decimal is [{user_val}]')
            case (10, 16): #dec to hex
                res = convert_decimal_to_hexadecimal(int(user_val))
                print(f'Input value in Hexadecimal is [{res}]')
            case (16, 2): #hex to bin
                res = convert_hex_to_binary(user_val)
                print(f'Input value in Binary is [{res}]')
            case (16, 8): #hex to oct
                x = convert_hex_to_binary(user_val)
                y = convert_binary_to_decimal(x)
                res = convert_decimal_to_octal(y)
                print(f'Input value in Octal is [{res}]')
            case (16, 10): #hex to dec
                x = convert_hex_to_binary(user_val)
                res = convert_binary_to_decimal(x)
                print(f'Input value in Decimal is [{res}]')
            case (16, 16): #hex to hex
                print("Hexadecimal to hexadecimal conversion really?")
                print(f'Input value in Hexadecimal is [{user_val}]')