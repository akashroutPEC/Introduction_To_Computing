# QUESTION-1: AVERAGE OF 3 NUMBERS

# first we take user input as a, b and c
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

# then we find average
avg=(a+b+c)/3

# finally we print average
print(avg)


# QUESTION-2: INCOME TAX CALCULATOR

# first we take the user's income and number of dependents as well as the fixed standard deduction
income=float(input("Enter your income to the nearest penny: "))
dependents=int(input("Enter number of dependents: "))
std_deduct=10000

# then we calculate the taxable income

taxable=income-std_deduct-3000*dependents

# finally we calculate the tax and print it
tax=0.2*taxable
print('$', tax)


# QUESTION-3: STUDENT DATA LIST

# first we take input from user
SID=input("Enter your Student ID: ")
name=input("Enter your name: ")
gender=input("Enter your gender: M for Male, F for Female, U for Unknown: ")
course_name=input("Enter your course: ")
CGPA=float(input("Enter your CGPA: "))

# then we make list and print it
list=[SID, name, gender, course_name, CGPA]
print(list)


# QUESTION-4: MARKS LIST

# first we take user input
m1=int(input("Enter marks of student 1: "))
m2=int(input("Enter marks of student 2: "))
m3=int(input("Enter marks of student 3: "))
m4=int(input("Enter marks of student 4: "))
m5=int(input("Enter marks of student 5: "))

# then we make list of marks
list=[m1, m2, m3, m4, m5]

# finally we sort the list and print it
list.sort()
print(list)


# QUESTION-5a: LIST ELEMENT REMOVAL

# first we provide the list
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# then we remove 4th element and print it
color.pop(3)
print(color)


# QUESTION-5b: LIST ELEMENT REPLACEMENT

# first we provide the list
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# now we replace the given elements and print the list
color.pop(3), color.pop(3), color.insert(3, 'Purple')
print(color)
