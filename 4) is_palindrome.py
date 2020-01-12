''' A PALINDROME IS STRING WHICH IS SAME IF REad from start or end
'''



word = input("Enter a word : ")

reverse = word[::-1]

if reverse == word:
      print("Is palindrome"
else:
      print("Not Palindrome")
      
      
      
=-------------------------------------------------------------------------------------------------------      

" sum of digits using while loop "




number = input("enter four digit number : ")

total = 0
x = 0
while x < len(number):
    total = int(number[x]) + total
    x = x+1

print(total)
