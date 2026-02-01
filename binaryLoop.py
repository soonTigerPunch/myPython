import os
binary=-1
loop=1
input_value=0
def exits():
    print("Exiting...")
    exit()
def plusBinary():
    global binary
    minus = input("How many to plus? ").strip()
    try:
        binary = binary + int(minus) -1
    except ValueError:
        print("invalid value, please enter a valid number")
def minusBinary():
    global binary
    minus = input("How many to minus? ").strip()
    try:
        binary = binary - int(minus) -1
    except ValueError:
        print("invalid value, please enter a valid number")

def welcome():
    os.system("cls")
    print("Welcome to Binary Loop!")
    print("This program will display binary numbers in a loop.")
    print("You can press Enter to see the next binary number, or type a number to start from there.")
    print("You can also type '+' or '-' to increment or decrement the binary number by a specified amount.")
    print("Type 'end' or 'exit' to quit the program.")
welcome()

while True:
    try:
        for i in range(loop):
            binary = binary + 1
            input_value = input().strip()
            key = input_value.lower()
            commands = {
                '-': minusBinary,
                '+': plusBinary,
                'end': exits,
                'exit': exits,
            }
            os.system("cls")
            if input_value == "":
                pass
            else:
                handler = commands.get(key)
                if handler:
                    handler()
                else:
                    try:
                        binary = int(input_value)
                    except ValueError:
                        print("invalid value, please enter a valid number")
            
            print(bin(binary).replace("0b",""), f"({binary})")
    except ValueError:
        print("invalid value, please enter a valid number")
