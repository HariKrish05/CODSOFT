# Looping
while True:
    # Title of the Project "Simple Calculator".
    print("~~~~~~~~~~~~Basic Calculator~~~~~~~~~~~~")

    
    # Getting two numbers from user.
    num1=(input("Enter the First Number Here: "))
    num2=(input("Enter the Second Number Here: "))
    
    # Checking number is numeric or not
    if (num1.isnumeric() and num2.isnumeric()):
        
        # Convert the inputs to floats.
        num1 = float(num1)
        num2 = float(num2)
        
        # Asking For choices.
        print("~~~~~~~~~~~~~~~Operations~~~~~~~~~~~~~~~")
        print(" Press 1 for Addition\n Press 2 for Subtraction\n Press 3 for Multiplication\n Press 4 for Division")
        print("~~~~~~~~~~~Select Your Choice~~~~~~~~~~~")
        choice=int(input("Enter Your Choice 1-4: "))

        print("~~~~~~~~~~~~~~~Calculation~~~~~~~~~~~~~~~")

        # Commands For Operations.
        if (choice==1):
            print("The Addition of ",num1," and ",num2," is ",num1+num2)
        elif (choice==2):
            print("The Subtraction of ",num1," and ",num2," is ",num1-num2)
        elif (choice==3):
            print("The Multiplication of ",num1," and ", num2," is ",num1*num2)
        elif (choice==4 and num2!=0):
            print("The Divison of ",num1," and ",num2," is ",num1/num2)
        elif (choice==4 and num2==0):
            print("The Divison of ",num1," and ",num2," is 'Infinity'")
    
        else:
            print("Invalid Choice Input Choose from 1-4")
        
        # Next Calculation 
        print("~~~~~~~~~~~~Next Calculation~~~~~~~~~~~~~~")
        next_calculation=input("Let's do next calculation? (yes/no): ")
        # break the loop
        if (next_calculation == "no"):
            break 
        
    # If the user input is not numeric
    else:
        print("Please Enter a Valid First number and Second number")    