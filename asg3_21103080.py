# ASSIGNMENT-3



# QUESTION 1
# COUNTING OCCURRENCES

# First we take user input of string
string=input("Enter your string: ")

# First we take take case for multiple word input
if " " in string:
    def word_count(str): # function word_count gives a dictionary containing occurrences of each word
        count=dict()
        words=str.split()
        for word in words:
            if word in count:
                count[word]+=1 # when word has already been counted once and is coming again
            else:
                count[word]=1 # when word comes for the first time
        return count
    print(word_count(string))

# Then we take case for single word output
else:
    def char_count(str): # function char_count gives a dictionary containing occurrences of each character
        count=dict()
        for char in string:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        return count
    print(char_count(string))



# QUESTION-2
# PRINTING NEXT DATE

# First we take user input of current date
day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))

# Condtions for Leap Year
if year%400==0:
    leap=True
elif year%100==0:
    leap=False
elif year%4==0:
    leap=True
else:
    leap=False

# Condtions for lengths of months
if month in (1,3,5,7,8,10,12):
    month_length=31
elif month in (4,6,9,11):
    month_length=30
elif month==2:
    if leap:
        month_length=29
    else:
        month_length=28
else:
    print("Invalid Date!")

if day<month_length: # if day is less than month length, day is increased by one
    day+=1
elif day==month_length: # if day is last day of month, next day is 1 and month is increased by one
    day=1
    if month==12: # case for New Year
        month=1
        year+=1
    else:
        month+=1
else:
    print("Invalid Date!")

print(f'Next Date is {day}/{month}/{year}')



# QUESTION-3
# LIST OF SQUARES

# First we take input of list from user
n=int(input("Enter length of list: "))
num_list=[]
for i in range(0, n):
    num=int(input(f'Enter number {i+1}: '))
    num_list.append(num)

output_list=[]
for i in range(0,n): # for all elements in list we find their squares
    square=num_list[i]**2
    tuple=(num_list[i], square) # here we make a tuple of element and its square
    output_list.append(tuple) # list of tuples

print(output_list)



# QUESTION-4
# GRADE AND PERFORMANCE

# First we take user input of grade
points=int(input("Enter the grade points between 4 and 10: "))

if points in range(4,11): # Condition for grade points to be from 4 to 10
    # list of grades and performances
    if points==10:
        grade="A+"
        performance="Outstanding"
    elif points==9:
        grade="A"
        performance="Excellent"
    elif points==8:
        grade="B+"
        performance="Very Good"
    elif points==7:
        grade="B"
        performance="Good"
    elif points==6:
        grade="C+"
        performance="Average"
    elif points==5:
        grade="C"
        performance="Below Average"
    elif points==4:
        grade="D"
        performance="Poor"
    print(f'Your Grade is {grade} and {performance} Performance.')
else:
    print("Invalid grade points!") # error message



# QUESTION-5
# ALPHABET PATTERN

# First we take user input for number of rows in pattern
rows=int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i): # printing spaces
        print(' ', end='')
    for j in range(2*(rows-i)-1):
        print(chr(65+j), end='') # printing characters, chr65 represents 'A' in ASCII and so on
    print() # for continuing in next line



# QUESTION-6
# DICTIONARY OPERATIONS

dictionary={} # this stores SID to name
while(True):
    command=input("Enter 'Y' to input SID and name of student or enter 'N' to continue: ")
    if command=='Y': # asks user for SID and name on entering 'Y'
        SID=int(input("Enter SID: "))
        name=input("Enter name: ")
        dictionary[SID]=name
        continue
    elif command=='N': # while loop is exited on entering 'N'
        break
    else:
        print("Enter valid input: ")

# PART-(A)
for key in dictionary: # prints keys and their values
    print(key, dictionary[key])

# PART-(B)
# name sorted dictionary
name_sorted_dict={}
SID_list1=list(dictionary.keys()) # list of SIDs
name_list1=list(dictionary.values()) # list of names
name_list1.sort() # sorts list of names
for name in name_list1:
    for SID in SID_list1:
        if(dictionary[SID]==name):
            name_sorted_dict[SID]=name # required dictionary
print(name_sorted_dict)

# PART-(C)
# SID sorted dictionary
SID_sorted_dict={}
SID_list2=list(dictionary.keys())
name_list2=list(dictionary.values())
SID_list2.sort() # sorts list of SIDs
for SID in SID_list2:
    for name in name_list2:
        if(dictionary[SID]==name):
            SID_sorted_dict[SID]=name # required dictionary
print(SID_sorted_dict)

# PART-(D)
num=int(input("Enter SID of student: "))
print(dictionary[num])



# QUESTION-7
# FIBONACCI SEQUENCE

# First we take user input for number of terms
num=int(input("Enter number of terms required: "))

def fibonacci(n): # this function finds terms of fibonacci sequence
    t1=0 # 1st term is 0
    t2=1 # 2nd term is 1
    sum=0
    for i in range(n):
        print(t1)
        sum+=t1 # updates the sum
        t3=t2+t1 # term(n+2)=term(n+1)+term(n)
        t1=t2 # values for finding next term
        t2=t3
    average=sum/n # finds average of sequence
    print(f'The average of sequence is {average}')
fibonacci(num) # gives the sequence and its average



# QUESTION-8
# OPERATIONS ON SETS

# Given sets
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

# PART-(A)
# Symmetric Difference of Sets
print(Set1^Set2)

# PART-(B)
print(Set1^Set2^Set3)

# PART-(C)
# Elements in exactly 2 sets
print(((Set1&Set2)|(Set2&Set3)|(Set3)&(Set1))-(Set1&Set2&Set3))

# PART-(D)
print({1,2,3,4,5,6,7,8,9,10}-Set1)

# PART-(E)
print({1,2,3,4,5,6,7,8,9,10}-Set1-Set2-Set3)