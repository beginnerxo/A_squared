'''INPUT : floating number
    OUTPUT: floating number

'''
# add two numbers. 
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
   
def pow(x, y):
    return x ** y

#cancel function: if user wrong to type, you cancel the action
def cancel():
    if #user click "cancel", the last value or operation will be deleted

#main method for calculations
def main():

    #Various operations in a list
    operation  = ["+","-","*","/"]
    
    #if user == +  
    
  
    '''accept the values for the calculations. 3 values to be exact needed here
        FIRST NUMBER, OPERATION, SECOND NUMBER
        
    '''
    firstValue = input("Enter the first value: ")
    input_operation = input("enter the operation")
    secondValue = input("enter the second value: ")

    
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
    else:
        print("This is invalid") 
    
        #use if and else statement to print out the appropriate operations and print out the correct values 
         
    
#main loop
    
if __name__ ==  "__main__":
    main()