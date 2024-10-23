days_in_year = 365.25
currency = input("Enter your currency: ")

#getting the P,R,T from the user

while True:
    try:
        principal = int(input("Enter amount borrowed: "))
        interest = float(input("Enter interest in %: "))/100
        time = int(input("Enter the time the loan is intended for: "))
    except ValueError:
        print("Enter correct values, borrowed amount - string, interest - integer, time - natural number")
    else:
        if principal>0 and interest >= 0 and time >0:
            break
        else:
            print("Enter positive values for amount borrowed, whole number for interest, positive value of time")

#will access these for the type of interval the user wants and divide 365.25 by these numbers for getting the intervals

interval_dict = {"d": ["Days", 1], "w": ["Weeks", 7], "m": ["Months",30.5833], "q": ["Quarters", 122.332], "y": ["Years", days_in_year]}

#functions


#how long to pay back?

def pay_time(amount, time, interval_key):
    while True:
        try:
            user = input("Do you wanna know when the loan will be paid? (Y/N): ")
        except ValueError:
            print("Enter string!")
        else:
            break
    if user.lower() == "y":
        while True:
            try:
                amount_intervally = int(input(f"Enter amount you will pay per {interval_key[:len(interval_key)-1:]}: "))
            except:
                print("Input proper integer")
            else:
                if amount_intervally != 0:
                    break
                else:
                    print("Enter a positive value")
        if amount%amount_intervally == 0:
            print("Under normal conditions, you will have paid the loan back in", int(amount/amount_intervally), interval_key)
        else:
            print(f"You would paid the loan back in {(amount//amount_intervally) +1}{interval_key}")
    else:
        print("Ok.")

#inputting the interval type (days/weeks.../years)

def get_valid_interval():
    while True:
        while True:
            try:
                interval = input("Enter interval type (Daily/Weekly/Monthly/Quaterly/Yearly). (D/W/M/Q/Y): ")
            except ValueError:
                print("Enter string!")
            else:
                break
        if interval.lower() in interval_dict:
            interval_key = interval_dict[interval.lower()][0]
            interval_type = interval_dict[interval.lower()][1]
            return interval_key, interval, interval_type
        else:
            print("Try again!")

#type of interests            

def compound():
    interval_key, interval, interval_type =get_valid_interval()
    amount = principal*(1+(interest/(days_in_year/interval_type)))**(time*interval_type/days_in_year)
    print(f"{currency}{amount:.2f} is needed to paid back")
    pay_time(amount, time, interval_key)

def simple():
    interval_key, interval, interval_type = get_valid_interval()
    amount = principal+ (principal*interest*time*interval_type/days_in_year)
    print(f"{currency}{amount:.2f} is needed to paid back")
    pay_time(amount, time, interval_key)


#compile

while True:
    while True:
        try:
            simple_compound = input("Compound or Simple Interest or Exit? (S/C/B): ")
        except ValueError:
            print("Enter string!")
        else:
            break
    
    if simple_compound.lower() == "s":
        simple()
    elif simple_compound.lower() == "c":
        compound()
    elif simple_compound.lower() == "b":
        print("Have days_in_year great day :)")
        break
    else:
        print("Enter valid input")