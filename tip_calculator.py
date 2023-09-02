'''
As the finance officer of Asanka Hotel, the food and beverages director has requested a program that calculates the total amount of a meal purchased with a fixed tip. 

Below are the requirements for the program:



The program should ask the user to enter the charge for the food.

It should then calculate the amounts of an 18 percent tip and 7 percent sales tax on the charge of the food and display each of these amounts.

Finally, it should add everything together and display the charge of the food plus tip and sales tax.

Based on this data, your program should generate script that meets the requirements. 

 

Below is an example execution of the program: 

input

Charge for food = $50.00



output

Tip = $9.00

Sales tax = $3.50

Grand total = $62.50
'''

def calculator():
 input1 = float(input("charge for the food"))
 tip = input1 * 0.18
 sales_tax = input1 *0.07
 grand_total = input1 + tip + sales_tax
 print("tip charge" , tip)
 print("sales tax" ,round(sales_tax, 2))
 print("grand total", grand_total)

result=calculator()
print(result)