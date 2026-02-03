import os
binary=-1
def exits():
    print("Exiting...")
    exit()
def plusBinary():
    global binary
    
    
    plus = input("How many to plus? ").strip()
    try:
        binary = binary + int(plus) -1
    except ValueError:
        print("Invalid value. Please enter a valid number.")
def minusBinary():
    global binary
    minus = input("How many to minus? ").strip()
    try:
        binary = binary - int(minus) -1
    except ValueError:
        print("Invalid value. Please enter a valid number.")
def multiyplyBinary():
    global binary
    multiply=input("How many to multiply? ").strip()
    try:
        binary=binary * int(multiply)-1
    except ValueError:
        print("Invalid value. Please enter a valid number.")
def divideBinary():
    global binary
    divide=input("How many to divide? ").strip()
    try:
        binary=binary // int(divide)-1
    except ValueError:
        print("Invalid value. Please enter a valid number.")
def uniCodeJump():
    global binary
    unicode_jump=input("Enter character or Unicode point (e.g., U+1F600): ").strip()
    try:
        if unicode_jump.startswith("U+"):
            code_point = int(unicode_jump[2:], 16)
            binary = code_point - 1
        elif len(unicode_jump) == 1:
            binary = ord(unicode_jump) - 1
        else:
            print("Invalid format. Please use 'U+XXXX' format or a single character.")
    except ValueError:
        print("Invalid value. Please enter a valid Unicode code point.")
   
    

def welcome():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to Binary Loop!")
    print("This program will display binary numbers in a loop.")
    print("You can press Enter to see the next binary number, or type a number to start from there.")
    print("You can also use the following commands:")
    print("'+' to add a number.")
    print("'-' to subtract a number.")
    print("'*' to multiply by a number.")
    print("'/' to divide by a number.")
    print("'u' to jump to a Unicode character or code point.")
    print("'end' or 'exit' to quit the program.")
    print("'help' to see this message again.")
welcome()

while True:
    try:
        input_value = input().strip()
        key = input_value.lower()
        commands = {
            '-': minusBinary,
            '+': plusBinary,
            '*': multiyplyBinary,
            '/': divideBinary,
            'u': uniCodeJump,
            'end': exits,
            'exit': exits,
            'quit': exits,
            'help': welcome,
        }
        binary = binary + 1 
        os.system("cls" if os.name == "nt" else "clear")
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
    except KeyboardInterrupt:
        exits()
