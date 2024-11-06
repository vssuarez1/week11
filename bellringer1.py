
# PROBLEM 1: Student Grade Categorization

scores = int(input("Enter student scores: ")) #asks for user input 
while scores < 0:     #checks if score is a negative and then continues the loop 
    print("Scores can't be negative.")          # prints this if score is negative
    scores = int(input("Enter student scores: ")) #asks for user input 
if scores >= 90 and scores <= 100:   # checks the scores and prints out the outcome of what score was entered
    print("Excellent")
elif scores >=70 and scores <= 89:     # for example, if score is between 70 - 89, it will print "Good"
    print("Good")
elif scores >= 50 and scores <= 69:
    print("Pass")
elif scores < 50:
    print("Fail")
    

 
    







# PROBLEM 2: Even and Odd Counter with Conditions

numbers= int(input("Enter a starting and ending number: ")) # asks for user input
start = 1   # start number
end = 100   # end number

count = 0
for number in range(start,end+1):   # for loop to iterate from the start and end number
    if number == 2:
        count == 1
    if number %2 == 0 and number > 10:     # checks if number is even and greater than 10
        print("Special even") 
    elif number < 20 and not number %2 == 0:   # checks if number is odd and less than 20 
        print("Special odd")



























