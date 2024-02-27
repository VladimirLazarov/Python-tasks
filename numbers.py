#uesers are asked to enter 3 different integers 
num1 = int(input("Enter the first integer:"))
num2 = int(input("Enter the second integer:"))
num3 = int(input("Enter the third integer"))

#calculation 

sum_of_all_the_numbers = num1 + num2 + num3
first_number_minus_second = num1 - num2
product_first_third = num3 * num1
sum_divded_by_third = (num1 + num2 + num3) / num3

# print 

print("Sum of all numbers:", sum_of_all_the_numbers)
print("First number minus the second number", first_number_minus_second)
print("Third number multiplied by the first number", product_first_third)
print("The sum of all three numbers divided by the third number", sum_divded_by_third)
