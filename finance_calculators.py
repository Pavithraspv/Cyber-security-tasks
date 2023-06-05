import math
'''added while loop to get the user input to check all possible flow of the given menu.If the user dont want to continue 
they can type any input other than investment and bond to exit the loop'''

while True:
    print("\ninvestment - to calculatethe amount of interest you will earn on your investment  \nbond - to calculate the amountyou will have to pay on a home loan\n")

    #Getting user input whether they are using investment service or bond service in the bank.
    user_input=input("Enter either 'investment' or 'bond' from the menu above to proceed :").lower()

    #If user entered the investment option the below code will be executed
    if user_input == "investment":
        principle_Amount=int(input("\nEnter the amount for deposit :"))
        interest_rate=int(input("enter the interest rate(note:enter only the number) :"))
        r=float(interest_rate/100)
        no_of_years=int(input("Enter the number of years, you plan on investment"))
        interest=input("do you want 'Simple' or 'Compound' interest,(hint:enter either 'simple' or 'compound' )").lower()
        #To calculate Simple interest
        if interest =="simple":
            A=principle_Amount*(1+r*no_of_years)
   
            print(f"Total amount when simple interest is applied for {no_of_years} years:{A}\n")
        #To calculate compound interest
        elif interest =="compound":
            amount=principle_Amount*math.pow((1+r),no_of_years)
            A=round(amount,2)
            print(f"Total amount when Compound interest is applied for {no_of_years} years :{A}\n")
        else:
            print("you did not entered valid input")
            
        continue
        #If user entered the bond option the below code will be executed
    elif user_input == "bond":
        Present_value_house=int(input("\nEnter the present value of the house :"))
        interest_rate=int(input("enter the interest rate :"))
        rate=float(interest_rate/100)
        monthly_interest=float(rate/12)
        no_of_months=int(input("Enter the number of months you plan to take to repay the bond :"))

        repayment=(monthly_interest*Present_value_house)/(1-(1+monthly_interest)**(-no_of_months))
        repayment=round(repayment,4)
        print(f"you have to pay monthly {repayment} for {no_of_months} months\n\n" )
        continue
    #To exit from the loop if the user type invalid input
    else:
        print("you did not entered the valid input.")
        break
    
    