'''INPUT : floating number
    OUTPUT: floating number

'''

# add two numbers.
import math
 
def add(x: float, y: float) -> float:
    addition = x + y
    return addition
   
#subtract two numbers
def sub(x, y):
   return x - y
   
#multiply two numbers
def mul(x,y):
    return x * y

#divide two numbers. Account for dividing with zeros also
def div(x,y):
    if (y == 0):
        return ("error")
    else:
        return x / y
    
def mod(x, y):
    if (y == 0):
        return "error"
    else:
        return x % y
   
def pow(x, y):
    return x ** y

def sqrt(x):
    if (x < 0):
        return "error"
    else:
        return math.sqrt(x)


#cancel function: if user wrong to type, you cancel the action
#def cancel():
    #if #user click "cancel", the last value or operation will be deleted

#main method for calculations
def main():

    #Various operations in a list
    operation  = ["+","-","*","/", "**", "%", "V"]
    
    '''accept the values for the calculations. 3 values to be exact needed here
        FIRST NUMBER, OPERATION, SECOND NUMBER  
    '''
    while True:
        try:
            firstValue = float(input("Enter the first value: "))
            input_operation = input("Enter the operation: ")
            
            if input_operation == "V" in operation:    
                    print(math.sqrt(firstValue))
                    go_or_not = input("Do you wish to continue/ input yes or no: ")
                    go_or_not.lower 

                    if go_or_not != "yes":
                        break
            else:
                secondValue = float(input("Enter the second value: "))

        # search for the input_operation in the list of operations 
        
                if input_operation in operation:
                    if input_operation == "+":
                        print(add(firstValue,secondValue))
                    if input_operation == "-":
                        print(sub(firstValue, secondValue))
                    if input_operation == "*":
                        print(mul(firstValue, secondValue))
                    if input_operation == "/":
                        print(div(firstValue, secondValue))
                    if input_operation == "**":
                        print(pow(firstValue, secondValue))
                    if input_operation == "%":
                        print(mod(firstValue, secondValue))
                    
                else:
                    print("This is invalid") 

                go_or_not = input("Do you wish to continue/ input yes or no: ")
                go_or_not.lower 

                if go_or_not != "yes":
                    break

        except ValueError:
            print("Error")
                #use if and else statement to print out the appropriate operations and print out the correct values 
            
    
#main loop
    
if __name__ ==  "__main__":
    main()