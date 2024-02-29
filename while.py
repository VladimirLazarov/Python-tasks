

# variables 
total = 0
count = 0
# keep asking the user to enter a number 
while True:
     
     #ask to user to input
    user_input = input("Enter a number (or -1 to stop): ")
     # if the user enter -1 to stop
    if user_input == "-1":
        break 
     # convert the input to a float and add to the total
    number = float(user_input)
    total += number 
    count += 1
# check if any numbers were entered 
if count > 0:
     # calculate
    average = total / count 
     #display the results 
    print(f"Average of the entered numbers: {average}")
else:
    print("No numbers entered.")