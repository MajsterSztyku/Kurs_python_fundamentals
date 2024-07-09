money_owed = float(input("how much money do  you owe?\n"))
apr = float(input("what is annual percentage rate of the loan?\n"))
payment = float(input("how much will you pay monthly in dollars?\n"))
months = int(input("for how many months do you want to see results?\n"))

monthly_rate = apr/100/12

intrest_paid = money_owed*monthly_rate

money_owed =  money_owed +intrest_paid

print("Paid ",payment," of witch ", intrest_paid,'was intrest')
print("Now I owe",money_owed)
