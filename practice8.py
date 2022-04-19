def max_two(a, b):
   if a>b:
       return a
   return b

def max_three(x, y, z):
    return max_two(x, max_two(y, z))

#print(max_three(62, 50, 3))
#==================================================================

list1 = [8, 2, 3, 0, 7, 12, 123]
def sum1(l):
    total = 0
    for i in l:
        total = total + i
    return total

#print(sum1(list1))
#===================================================================

list2 = [8, 2, 3, -1, 7]
def mul(l):
    total = 1
    for i in l:
        total = total * i
    return total

#print(mul(list2))
#=====================================================================

def rev_string(str1):
    rstr1 = ' '
    index = len(str1)
    while index > 0:
        rstr1 = rstr1 + str1[index - 1]
        index = index - 1
    return rstr1


#print(rev_string('1234abcd'))
#=======================================================================

lst = [1,2,3,3,3,3,4,5]
UniqueList = [1, 2, 3, 4, 5]

def unique_lst(lst):
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    return x

#print(unique_lst(lst))
#==========================================================================

def check(num):
    if num in range(100):
        print("Present in range.")
    else:
        print("Absent in range. ")
    return num


#num = int(input("Enter the number: "))
#print(check(num))
#=================================================================================

def counting(str):
    uppercase = 0
    lowercase = 0
    for c in str:
        if c.isupper():
            uppercase += 1
        elif c.islower():
            lowercase += 1
    return uppercase, lowercase

#str = 'The quick Brown Fox'
#print(counting(str))

#===============================================================================
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#n = int(input("Enter the number: "))
#print(factorial(n))
#================================================================================

def prim(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
            return True

#print(prim(14))
#====================================================================================

def palindrome(str):
    if str[::] == str[::-1]:
        return "String is palindrome"
    else:
        return "String in not palindrome"

str = 'maddam23'
#print(palindrome(str))
#=================================================================================
def abcd():
    a = 23
    bk = 56
    cd = 'Priya'

print(abcd.__code__.co_nlocals)
#===================================================================================
#Constuctor

class Priyanka:

    def __init__(self):
        self.name = "Priyanka"

    def print_Pri(self):
        print(self.name)

obj = Priyanka()
obj.print_Pri()
#===========================================================================

class Addition:
    fno = 0
    sno = 0
    answer = 0

    def __init__(self, fno, sno):
        self.fno = fno
        self.sno = sno


    def display(self):
        print("Answer is: " + str(self.answer))

    def calculate(self):
        self.answer = self.fno + self.sno


obj = Addition(50, 60)
obj.calculate()
obj.display()












