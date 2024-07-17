import math
x = 0
y = 0
while True:
    
    inpt = input("")
    if inpt=="STOP":
        break
    instructions = inpt.split(" ")
    if instructions[0]=="RIGHT":
        x+=int(instructions[1])
    elif instructions[0]=="LEFT":
        x-=int(instructions[1])
    elif instructions[0]=="UP":
        y+=int(instructions[1])
    elif instructions[0]=="DOWN":
        y-=int(instructions[1])
    
print(int(math.sqrt(x*x+y*y)))