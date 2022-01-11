num1 = float(input("Please enter a number -"))
num2 = float(input("Please enter your second number - "))

opr = str(input("Please enter your math operation (+,-,*,/) = "))

if opr == "+":
    total = num1 + num2
elif opr == "-":
    total = num1 - num2
elif opr == "*":
    total = num1 * num2
elif opr == "/":
    total = num1 / num2
else:
    total = str("Please enter a valid math operation")
    
print(total)    
    
    