'''String Manipulations :- '''

fname = input("Enter your Name :")
lname = input("Enter your Surname : ")

full_name  =  fname + " " + lname

print(full_name)

OR

print(fname + lname)


################################

name = "bhavitavaya"
age = 24
surname = "shrivastava"
pin = 440012
print("hello {} your age {}".format(name,age))

print(f"hello {surname} your pincode {pin}")



####################################
" Find out Average of 3 Numbers console input

num1 = input("Enter number : ")

num2 = input("Enter number : ")

num3 = input("Enter number : ")

avg = (int(num1)+int(num2)+int(num3)) / 3


print(f"Average of three numbers is : {avg}")
