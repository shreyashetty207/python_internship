# Create a function covid( ) & it should accept patient name, and body temperature,by default the body temperature should be 98 degree
def covid(name,temp=98):
    print("Patient name :",name)
    print("Temperature:",temp)
a = input("Enter patient name -")
b = input("Enter body  temperature -")
covid(a,b)
