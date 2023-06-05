#OS module in Python provides functions for interacting with the operating system (to check the status of the file size)
import os    

#initialisation of variables
file_name=None
result=0
equation=""
user_file_name=""
ans=None

# starting of the Code to get the file name from the user to store the equation

while True:
    #used try and exception block to handle invalid inputs from the user
    try:
       
        user_file_name=input("Enter the file name to store the equations  :")
        user_file_name_with_format=user_file_name +".txt"
        print(user_file_name_with_format)
        if os.path.isfile(user_file_name_with_format):
            raise FileExistsError
        #user_file_name=create_file(user_file_name)
        if user_file_name !=None:
            break
    
    except FileExistsError:
        print("Entered file name already exists ,please give different file name") 
        continue
    except Exception:
        print("you have not entered a valid file name,please enter valid file name")


# ending  of the Code to get the file name from the user to store the equation




#---start of code for getting name of the file to store the equations 
try:
    #to create new file and store the equation
    def create_file(user_file_name_with_format):

        file_name=open(user_file_name_with_format,"x")
        file_name.close
        file_name=open(user_file_name_with_format,"w")
        #file_name.write(equation+"\n")
        file_name.write(equation)

      #  file_name=open(user_file_name+".txt","r")
      #  text=file_name.read()
       # print(text)
        return user_file_name_with_format
    
    def append_file(user_file_name,equations):
        file_name = open(user_file_name, "a")
        file_name.write(equations)
        #file_name.write(equations+"\n")
        file_name.close
        print("\n")
        return user_file_name
    
    def open_file(user_file_name):
            file_name=open(user_file_name,"r")
            #When a user attempts to read from file, the file is empty
            if os.stat(user_file_name).st_size > 0:
                #print(str(os.stat(user_file_name).st_size))
                print(file_name.read())
                file_name.close
            else:
                print("file is empty there is no equation to display.\n")

except FileExistsError:
    print("Entered file name already exists ,please give different file name")            
except FileNotFoundError:
    print("The file you are tring to open does not exist")
# Checking whether file are saving to a file successfully and reading from the file successfully.
# #correction 3 rectified
except IOError as e:
    print("IO excetpion occured :"+e)
finally:
    if file_name is not None:
        file_name.close
#----end of code for getting name of the file to store the equations from the user

def calculation():
#code to get the user input
    while True:
    #used try and exception block to handle invalid inputs from the user
        try:
            num1=int(input("enter a 1st number :"))
            num2=int(input("enter a 2nd number :"))
            operation=input("the operation(E.g. +,-,x etc) you would like to perform :")
            if operation == "+" or operation == "-" or operation == "x" or operation == "/":
                break
            else:
            #if user didnt enter the basic operation symbols,this code will handle the customised exception 
                raise Exception
        except ValueError:
            print("you have not entered a valid number,please enter a valid number to continue") #correction 1 rectified
        except Exception:
            print("you haven't entered valid symbol for calculation")
#functions to handle simple calculations 
    def add(num1,num2):
        return num1 + num2
    def subtraction(num1,num2):
        return num1 - num2
    def multipy(num1,num2):
        return num1 * num2
    
    def divide(num1,num2):
        try:
            print("number 1 and number 2 :"+str(num1)+" "+str(num2))
            ans=num1 / num2
            return ans
        
        except ValueError:
                print("Enter valid number for calculation")
                #correction 2 rectified
        except ZeroDivisionError as zerodivitionerror:
                print("you have entered zero which results in zero division exception")
                print(zerodivitionerror)    

#code to find the operation based on the user input
    if operation == "+":
        result=add(num1,num2)
    elif operation == "-":
        result=subtraction(num1,num2)
    elif operation == "x":
        result=multipy(num1,num2)
    elif operation == "/":
            result=divide(num1,num2)
              

    if result is not None:
        equation="equation is "+str(num1)+" "+operation+" "+str(num2)+" = "+str(result)+"\n"
        print("\n")
    else:
        equation=""

    return equation




def select_your_operation():
    while True:
    #used try and exception block to handle invalid inputs from the user
        try:
        
            menu = int(input("Please select your option from following: \n 1.Do calculation  \n 2.Read the equation from the file \n 3.Exit \n (Eg: Press 1 for calculation or 2 for reading equation) "))
            if menu == 1 or menu == 2 or menu ==3 :
                break
            else:
                print("Enter valid number from the menu to proceed")
                continue
            
        except ValueError:
            print("you have not entered a valid number,please give a valid number to continue")
    return menu

#code to call the function for creating new file  
user_file_name=create_file(user_file_name_with_format)
print("user file name is :"+user_file_name)
menu=select_your_operation()


while True:
    if menu ==1:
        #print("before calculation")
        equations=calculation()
        #print("after calculation")
        print(equations)
        menu=select_your_operation()
        user_file_name=append_file(user_file_name,equations)
        continue
    elif menu ==2:
        #print("before opening file")
        open_file(user_file_name)
        #print("after opening file")
        menu=select_your_operation()
        continue
    elif menu ==3:
        print("you are succesfully exited from the code")
        break




#reference:https://www.geeksforgeeks.org/python-os-stat-method/
