num = int(input("Enter a decimal number: "))


def dec_bin(num):
    if(num >= 1):
        dec_bin(num//2)
    print(num % 2, end='')


def dec_oct(num):
    if(num >= 1):
        dec_oct(num//8)
    print(num % 8, end='')


def dec_hex(num):
    conversion_table = [0, 1, 2, 3, 4, 5, 6, 7,
                        8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    if(num > 0):
        dec_hex(num//16)
    print(conversion_table[num % 16], end='')


choice = int(input(
    "Enter your choice:\n1.Decimal To Binary\n2.Decimal To Octal\n3.Decimal To Hexadecimal\n"))
if(choice == 1):
    dec_bin(num)
elif(choice == 2):
    dec_oct(num)
elif(choice == 3):
    dec_hex(num)
