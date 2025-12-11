'''
WAP to take marks from the user and just print the grade for that marks.
-- 100 - 90: A+
-- Less than 90 and greater or equal to 70: A
-- Less than 70 and greater or equal to 60: B
-- Less than 60 and greater or equal to 40: C
-- Below 40: Fail

'''

# marks = int(input('Enter a number: '))
# if marks >= 90 and marks <= 100:
#     print('A+')
# elif marks >= 70 and marks < 90:
#     print('A')
# elif marks >= 60 and marks < 70:
#     print('B')
# elif marks >= 40 and marks < 60:
#     print('C')
# elif marks < 40:
#     print('Fail')




'''
WAP to take a number from the user and check whether it is a positive or negative or zero.
'''
# num = int(input('Enter a number: '))
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('negative')
# elif num == 0:
#     print('Zero')
    
    
    
 
# n = int(input('Enter a number: '))

# if n > 90:
#     print('Hello1') # stop execution
# elif n > 70:
#     print('Hello2')
# elif n > 50:
#     print('Hello3')
# elif n > 30:
#     print('Hello4')
# elif n > 0:
#     print('Hello5')   





'''
Write a program to check the grade of a student based on marks.
-- The user will enter marks out of 100.
-- If marks are 90 or above, print "Excellent".
-- If marks are between 80 and 89, print "Very Good".
-- If marks are between 70 and 79, print "Good".
-- If marks are below 70, print "Needs Improvement".
'''
# n = int(input('Enter a number: '))
# if n >= 90:
#     print('Excellent!')
# elif n >= 80:
#     print('very Good!')
# elif n >= 70:
#     print('Good')
# elif n < 70:
#     print('Needs Improvement!')
    


'''
Write a program to categorize temperature.
-- User enters the temperature in °C.
-- If temperature > 40, print "Very Hot".
-- If temperature > 30, print "Hot".
-- If temperature > 20, print "Warm".
-- If temperature > 10, print "Cool".
-- Else print "Cold".
'''

'''
Write a program to check the type of day based on number.
--- The user enters a number from 1 to 7.
--- If the number is 1, print "Monday".
--- If 2, print "Tuesday".
--- If 3, print "Wednesday".
--- If 4, print "Thursday".
--- If 5, print "Friday".
--- If 6, print "Saturday".
--- If 7, print "Sunday".
Else print "Invalid Input".
'''
# day_no = int(input('Enter a day no between 1 to 7: '))
# if day_no == 1:
#     print('Monday!')
# elif day_no == 2:
#     print('Tuesday!')
# elif day_no == 3:
#     print('Wednesday!')
# elif day_no == 4:
#     print('Thursday!')
# elif day_no == 5:
#     print('Friday!')
# elif day_no == 6:
#     print('Saturday!')
# elif day_no == 7:
#     print('Sunday!')
# else:
#     print('Invalid Day No!')



'''
Write a program to take 2 numbers from the user. Along with take the operator from the user.
-- perform addition if user passes "+"
-- perform subtraction if user passes "-"
-- perform multiplication if user passes "*"
-- perform division if user passes "/"
'''
n1, n2, op = int(input('First Number: ')), int(input('Sec Number: ')), input('Enter operator: ')
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print('Invalid Operator!')


'''
Write a program to classify a character input by the user.
-- The user enters a single character.
-- If it is a vowel (a, e, i, o, u, A, E, I, O, U) → print "Vowel".
-- If it is an alphabet but not a vowel → print "Consonant".
-- If it is a digit, print "Digit".
-- Else print "Special Character".
'''

# char = input('Enter a character: ')
# if char in 'aeiouAEIOU':
#     print('Vowel!')
# elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
#     print('Consonent!')
# elif char in '0123456789':
#     print('Digit')
# else:
#     print('Special Character!')