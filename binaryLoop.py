import os
binary=-1
loop=1
input_value=0
os.system("cls")
print("Press Enter to see the next binary number. or type number to start from there. Type end to exit.")
while True:
    try:
        for i in range(loop):
            binary=binary+1
            input_value = input()
            if input_value.lower() == "end" or input_value.lower() == "exit":
                exit()
            if input_value.strip() != "":
                binary=int(input_value)
            os.system("cls")
            print(bin(binary).replace("0b",""),f"({binary})")
    except ValueError:
        print("invalid value, please enter a valid number")