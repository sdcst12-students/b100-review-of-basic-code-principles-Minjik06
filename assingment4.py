"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""
a=int(input("initial debt? : "))
b=float(input("annual interest rate? : "))
b=b/100
c=int(input("monthly payments? : "))
month=0
totalp=0
i=0

while a!=0 and a>0:
    month+=1
    debt=a+a*b
    i+=a*b
    left = debt-c
    a=left
print(f"{month} months")
print(f"He will have paid {round(i,2)} in interest")
