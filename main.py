#My Personal Python calculator
def Greetings():
    print('''Welcome to My Personal Calculator\n''')
...

Greetings()

def calculate():
# Store number variables for the two numbers
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
# Calculation of the two numbers
    print("Addition: ", '{} + {} = '.format(a, b), (a+b))
    print("Subtraction: ", '{} - {} = '.format(a, b), (a-b))
    print("Multiplication: ", '{} * {} = '.format(a, b), (a*b))
    print("Division: ", '{} / {} = '.format(a, b), (a/b))
    return
calculate()

print("\nThank You For Using My Personal Calculator")