'''
Simple calculator app: add, subtract, multiply, divide
'''
print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input("Enter your choice: ")
# operation= input()
# print("Selected Operation:", operation)

if operation== "add":
    print("Enter two numbers: ")
    num1=input("First number: ")
    num2=input("Second number: ")
    # sum= num1+num2
    print("Sum is", int(num1)+ int(num2))
    
elif operation== "subtract":
    print("Enter two numbers:")
    num1=input("First number: ")
    num2=input("Second number: ")

    diff=int(num1)- int(num2)
    print("Difference is", diff)  
    
elif operation== "multiply":
    print("Enter two numbers:")
    num1=input("First number: ")
    num2=input("Second number: ")
    # mul = int(num1) * int(num2)
    # print("Multiplied answer is", mul)
    print("Multiplied answer is "+ str(int(num1) * int(num2)))
elif operation== "divide":
    print("Enter two numbers: ")
    num1=input("First number: ")
    num2=input("Second number: ")
    div= int(num1)/int(num2)
    rem= int(num1)% int(num2)
    print("Divided answer is ", div)
    print("Reminder is ", rem)
    
else:
    print("Invalid operation")
