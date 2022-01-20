# QUESTION-1

string='Python is a case sensitive language.'

# PART-(A)
# We use len() function to find string length
print(len(string))

# PART-(B)
# We reverse tthe order of the string
print(string[len(string)::-1])

# PART-(C)
# Slicing of string
print(string[10:26])

# PART-(D)
# String replacement
print(string.replace("a case sensitive", "object oriented"))

# PART-(E)
# String index
print(string.index("a"))

# PART-(F)
# String removal
print(string.replace(" ", ""))


# QUESTION-2
# STRING FORMATTING

# First we take input of data from user
name=input("Enter your name: ")
SID=input("Enter your SID: ")
dep_name=input("Enter your department name: ")
CGPA=input("Enter your CGPA: ")

# Then we print the output using string formatting
print(f'Hey, {name} Here!')
print(f'My SID is {SID}')
print(f'I am from {dep_name} department and my CGPA is {CGPA}')


# QUESTION-3

a=56
b=10

# PART-(A)
print(a&b)

# PART-(B)
print(a|b)

# PART-(C)
print(a^b)

# PART-(D)
print(a<<2)
print(b<<2)

# PART-(E)
print(a>>2)
print(b>>4)


# QUESTION-4
# GREATEST OF THREE NUMBERS

# First we take input of 3 numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

# Then we compare the numbers and print the greatest one
if (a>b):
    if (a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)


# QUESTION-5
# CHECKING PRESENCE OF "NAME"

# First we take user input
string=input("Enter your string: ")

# Then we check if "name" is present in string or not
if "name" in string:
    print('Yes')
else:
    print('No')


# QUESTION-6
# CHECKING FOR TRIANGLE

# First we take sides from user
a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))

# Then we check the condition for triangle
if((a+b)>c and (b+c)>a and (c+a)>b):
    print('Yes')
else:
    print('No')