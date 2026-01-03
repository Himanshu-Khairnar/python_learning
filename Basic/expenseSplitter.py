def billSpitter(totalBillAmount,totalPerson,tipPercentage):
    tip = totalBillAmount * (tipPercentage/100)
    total = tip+totalBillAmount
    personPersonSplit = total/totalPerson
    
    print(f"Final bill including tip is {total} and per person each one has to pay {personPersonSplit}")

totalBillAmount = int(input("Enter the total bill amount: "))
totalPerson = int(input("Enter the total number of person amount to be splited: "))
tipPercentage = int(input("Enter the tip percentage you wanna pay to the waiter: "))

billSpitter(totalBillAmount,totalPerson,tipPercentage)