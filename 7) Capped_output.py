'''
Three equation are capped for a given output 

but rest function should be executed normally 

 Given these three calculations are capped for output :
#  45 * 3 = 555

#  56 + 9 = 76

#  56/6 = 5

'''

num1 = int(input("Enter your first number : "))
operator = input("enter your operator : ")
num2 = int(input("Enter your second number : "))

if (num1 ==45 and num2 == 3) and operator == '*':
    print("555")
elif (num1 ==56 and num2 == 9) and operator == '+':
    print(76)

elif (num1 ==56 and num2 == 6) and operator == '/':
    print(5)
elif operator == "+":
    print(num1+num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
elif operator == "**":
    print(num1**num2)

