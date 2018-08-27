#Q.1) Name and handle the exception occured in the following program
print("The Exception Occured is ZeroDivisionError\n") 

a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:        
        print("The Division cannot be done by 0.\n")

#Q.2- Name and handle the exception occurred in the following program:  l=[1,2,3]  print(l[3])

print("The Exception Occured is IndexError.\n")

l=[1,2,3]
try:
    print(l[3])
except:
    print("The Index of the list starts from 0 and is less than the total length of the list")
    print(l[2])
    
#Q.3- What will be the output of the following code:

print("OUTPUT OF THE CODE\n")
print("'An Exception' Will be printed after that an NameError eception is occured")

#Q.4- What will be the output of the following code:

print("OUTPUT OF THE CODE\n")

print('-5.0')
print('a/b result in 0')

#Q.5- Write a program to show and handle following exceptions: 1. Import Error 2. Value Error 3. Index Error

print('1.) IMPORT ERROR\n')

''' import sys
sys.modules['os']= None
import os   '''


print('Handling Exception\n')

try:
    import sys
    sys.modules['os']=None
    import os
except ImportError:
    print(sys.modules['os'])
    
print('\n2.) VALUE ERROR\n')

''' print(int("A")) '''

print('Handling Exception\n')

try:
    print(int("A"))
except ValueError:
    print(ord("A"))
    
print('3.) INDEX ERROR\n')

'''  list=[1,2,3,4,5]

print(list[8])  '''

print('Handling Exception\n')

list=[1,2,3,4,5]

try:
    print(list[8])
except IndexError:
    print("The Index of the list starts from 0 and is less than the total length of the list")
    print(list[3])
