'''
Write a program in python to take one number from the user. Then check whether the number is 0 or not. If the number is 0 then print "it is a zero". If the number is not 0 then print "It is not zero".
'''
# 1. I have to take one number from the user.
# 2. Check the condition.

# num = int(input('Enter a number: '))
# # When the output of the condition will be True
# if num == 0:
#     print('It is a zero') # TSB
# else:
#     print('It is not a zero') # FSB




# Write a Python program where the user enters a number and the program checks whether the number is positive or negative and then prints the appropriate message.
'''
Algorithm:
-- I should take the number from the user.
-- Now I have to check condition on that number.
-- if the number is a "Positive Number", print "Positive"
-- If "Negative Number", print "negative".
'''
# num = int(input('Enter a number: '))
# if num > 0:
#     print('Positive')
# else:
#     print('Negative')


# Create a program that asks the user to enter a number and checks whether the number is even or odd, and then prints the result.
# if, num % 2 == 0, It is an even number. Otherwise, odd number.

n = int(input('Enter a number: '))
if n % 2 == 0:
    print('Even number')
else:
    print('Odd number')

# Write a program that accepts the user’s age as input and checks whether they are eligible to vote. If the age is 18 or more, display “You are eligible to vote”, otherwise display “You are not eligible to vote”.


# Write a Python program where the user inputs two numbers. Compare the two numbers and print which one is greater.


# Create a program that takes a number as input and checks if the number is divisible by 5. If it is divisible, print “Divisible by 5” otherwise print “Not divisible by 5”.


# Write a program where the user enters their exam score. If the score is greater than or equal to 40, print “Pass”, otherwise print “Fail”.


# Write a Python program that asks the user for a number and checks whether the last digit of the number is 3. If the last digit is 3, print “Last digit is 3” otherwise print “Last digit is not 3”.
n = int(input('Enter a number: '))
if str(n)[-1] == '3':
    print('Last digit is 3!')
else:
    print('Last digit is not three!')

# Create a program that accepts a number and checks whether it lies between 1 and 100 (inclusive). If it lies in that range, print “Number is in range”, otherwise print “Number is out of range”.


# Write a program that takes a year as input and checks whether it is a leap year or not. A leap year is a year that is divisible by 4. Print the result accordingly.
'''
Algorithms:
-- Take year from the user.
-- Check the condition. year % 4 == 0.
-- If it is leap year, print "Leap Year"
-- If not, print "Not a Leap Year"
'''

# Create a program that asks the user to enter a password. If the entered password matches the predefined password “python123”, print “Access Granted”, otherwise print “Access Denied”.