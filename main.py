import math

print("Select an operation to perform")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIvide")
print("5. CUBE ROOT")
print("6. RAISE TO POWER")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input ('Enter second number: ')
    print("The sum is: " + str(int(num1) + int(num2)))
    
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: " )
    print("The subtract is: " + str(int(num1) - int(num2)))

elif operation =="3":
    num1 = input("Enter first number: ")
    num2 = input("Enter Second number: ")
    num3 =input("Enter the third digit or number: ")

    print("The multplication output: " + str(int(num1) * int(num2) * int(num3))) 

elif operation =="4":

    num1 = input("Enter the first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third digit: ")

    print("The output is: " + str(int(num1) / int(num2) / int(num3)))

elif operation =="5":

    num = int(input("Enter the number: "))
    

    print("The output is %f " %(math.sqrt(num)) )

elif operation =="6":

    num = int(input("Enter the number: "))

    print("The output is %d " %(pow(num , 3)))

else:
    print("Invalid Function number")
     
  