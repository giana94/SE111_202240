#Giana Hardin
#Lab 2A
#04/16/2022 
#Program Essentials with Python, 202230_SE116.01

#PROGRAM PROMPT: You want to develop a program that gathers the user’s hourly pay, weekly hours worked, and tax rate for a two-week period. Once you have this information, you want to display the user’s Gross Pay, Uncle Sam’s Share (the amount to be removed for taxes), and the User’s Net Pay. All calculations should be limited to run once, rather than numerous times. Include in your flowchart the use of variables and print statements. Use 20% for the tax rate. 

#VARIABLE DICTIONARY:

#hourly_rate    Money per hour [User input]
#hoursPerWeek   Hours worked per week [User input]
#tax_rate       Uncle Sams share of your final pay [Use 20% or .2]
#gross_pay      Amount of money made before taxes
#uncleSam       tax rate to be subtracted from gross pay
#net_pay        Amount of money made after taxes

#CALCULATIONS
#gross_pay = hourly_rate * hoursPerWeek, $$
#UncleSam = gross_pay * tax_rate, $$
#net_pay = gross+pay * tax_rate, $$

#twoWeekNetPay = net_pay * 2, $$

#NOTES

#----------MAIN PROGRAM CODE----------

print("\n\t\tHello!")
print()

hourly_rate = float(input("\nHow much do you make an hour?: $ "))

print()

hoursPerWeek = float(input("How many hours a week do you work?: "))

print()

#use 20% for tax rate but prompt user to input tax rate as a decimal

tax_rate = float(input("What is the current tax rate? (please input percentages as decimals): "))

gross_pay = hourly_rate * hoursPerWeek

print("\n\n\n\tBased on your information, here is your expected pay")

print("\n\n\t\t\t\t Weekly grossed pay: ${:.2f}".format(gross_pay))

uncleSam = gross_pay * tax_rate

print("\n\t\t\tUncle Sam tax deduction: $ {:.2f}".format(uncleSam))

net_pay = gross_pay - uncleSam

print("\n\t\t\t\t  weekly net pay is: ${:.2f}".format(net_pay))

twoWeekNetPay = net_pay * 2

print("\n\t\t\t\t  Bi-weekly net pay: ${:.2f}".format(twoWeekNetPay))

print("\n\n\t\tHave a great day! Goodbye!")