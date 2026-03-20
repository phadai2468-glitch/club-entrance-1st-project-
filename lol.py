operarion = input ("what operation do you want to perorm(+ - * /)")
num1 = float(input(("enter number 1 ")))
num2 = float(input(("enter number 2 ")))
if operarion == "+":
    print (round (num1 + num2,2))

if operarion == "-":
    print (round (num1 - num2,2))

if operarion == "*":
    print (round (num1 * num2,2))

if operarion == "/":
 print (round (num1 / num2,2))