str_manip = input("Enter a sentence: ")
lenght_of_str = len(str_manip)
print("Enter a sentence: ",lenght_of_str)
#last letter
last_letter = str_manip[-1]
print(last_letter)
#Reaplce every occurrence with @
str_manip_modified = str_manip.replace(last_letter, '@')
print("Modified str_manip:",str_manip_modified)

five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:",five_letter_word)
