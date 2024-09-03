
# This program:
# asks the diner how much they spent on dinner;
# ask for the diner's satisfaction level using these ratings:
# 1 = totally satisfied, 2 = satisfied, 3 = dissatisfied;

# then calculates tip:
# if the diner is totally satisfied, calculate a 20% tip
# if the diner is satisfied, calculate a 15% tip
# if the diner is dissatisfied, calculate a 10% tip;

# then reports satisfaction level and tip in dollars and cents.


dinnerBill = 0
satisLvl = 0
tipAmount = 0


#Prompt user to input bill amount.
dinnerBill = input("How much did you spend at dinner? ")
dinnerBill = float(dinnerBill)
# Catch input errors.
if dinnerBill <= 0 :
    print(" ")
    print("Error: please enter the total dinner bill. ")
    print(" ")
    dinnerBill = input("How much did you spend at dinner? ")
dinnerBill = float(dinnerBill)
print(" ")

# Prompt user to select satisfaction level.
print("How satisfied are you with your service? ")
print("1 = Totally satisfied ")
print("2 = Satisfied ")
print("3 = Dissatisfied ")
satisLvl = input("")
satisLvl = int(satisLvl)

# Calculate tip by percent of total bill via satisfaction level.
if satisLvl == 1 :
    tipAmount = dinnerBill * 0.20
elif satisLvl == 2 :
    tipAmount = dinnerBill * 0.15
else :
    satisLvl == 3
    tipAmount = dinnerBill * 0.10
tipAmount = round(tipAmount, 2)
# Use function to force resulting display to two decimal places for currency.
tipAmount = (f"{tipAmount:.2f}")
print(" ")

# Display calculated tip amount and corresponding satisfaction level.
if satisLvl == 1 :
    print("You entered: Totally satisfied ")
    print("Tip: ", "$", tipAmount)
elif satisLvl == 2 :
    print("You entered: Satisfied ")
    print("Tip: ", "$", tipAmount)
else :
    satisLvl == 3
    print("You entered: Dissatisfied ")
    print("Tip: ", "$", tipAmount)

    
