def Greetings():
    print('''
Welcome to Calculator
''')
...

Greetings()

def calculate():
# Store number variables for the two numbers
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Addition: ", '{} + {} = '.format(a, b), (a+b))
    print("Substration: ", '{} - {} = '.format(a, b), (a-b))
    print("Multiplication: ", '{} * {} = '.format(a, b), (a*b))
    print("Division: ", '{} / {} = '.format(a, b), (a/b))
    return
calculate()