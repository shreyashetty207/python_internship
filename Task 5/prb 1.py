#Create a function getting two integer inputs from user. & print the following:
#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value
def op(a,b):
    print(" Addition of two numbers  is ",a+b)
    print("SUbtraction of two number is ",a-b)
    print("Multiplication of two number is ",a*b)
    print("Division of two number is",a//b)
x=int(input("First number="))
y=int(input("second number="))
op(x,y)
