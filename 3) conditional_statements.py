''''''''''''''''''''' for loop ''''''''''''''''''''''

sum of digits of number entered from console

eg : 356 ----->  3+6+5 = 14
'''''''''''''''''''''''''''''''''''''''''''''''''''''

number = input(" Enter a number : ")

sum = 0
for i in range(len(number)):
    sum = int(number[i]) + sum

print(f"Sum of all the digits is : {sum}")


''''''''''''''''''''''''''''''''''''''''''''''''''''''
with while loop 
'''''''''''''''''''''''''''''''''''''''''''''''''''''

number = input("enter four digit number : ")

total = 0
x = 0
while x < len(number):
    total = int(number[x]) + total
    x = x+1

print(total)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
