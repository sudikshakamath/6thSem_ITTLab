num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = int(input("Enter the choice:\n1. Add \n2. Subtract \n3. Divide \n4.Multiply\n"))

if(op == 1):
    print(num1+num2)
elif(op == 2):
    print(num1-num2)
elif(op == 3):
    print(num1/num2)
elif(op == 4):
    print(num1*num2)
