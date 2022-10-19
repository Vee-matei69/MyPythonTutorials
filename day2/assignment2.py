#taking marks from the user
maths = int(input('Enter your math marks: ' ))
english = int(input('Enter your english marks: ' ))
kiswahili = int(input('Enter your kiswahili marks: ' ))

#calculate total marks
total_marks = maths + english + kiswahili

#calculate average
average_marks = total_marks * 0.3333

#displaying total marks
print('\n')
print('Your total marks is: ', total_marks)

#display average marks
print('Your average marks is: ', average_marks)

#grading
print('\n')
if maths > 70:
    print('Your math grade is A. ')
elif maths > 50:
    print('Your maths grade is B. ')  
elif maths > 30:
    print('Your maths grade is C. ')
else:
    print('Your maths grade is D! ') 

#ENGLISH
if english > 70:
    print('Your english grade is A. ')
elif english > 50:
    print('Your english grade is B. ')  
elif english > 30:
    print('Your english grade is C. ')
else:
    print('Your english grade is D! ') 

#kiswahili
if kiswahili > 70:
    print('Your kiswahili grade is A. ')
elif kiswahili > 50:
    print('Your kiswahili grade is B. ')  
elif kiswahili > 30:
    print('Your kiswahili grade is C. ')
else:
    print('Your kiswahili grade is D! ')  

#grading overall
print('\n')
if average_marks > 72:
    print('Your overall grade is A. ')
elif average_marks > 62:
    print('Your overall grade is B. ')
elif average_marks >52:
    print('Your overall grade is C. ')  
else:
    print('Your overall grade is D. ')        



