#NAMES
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    value = second_func()
    return value

def second_func(d=40):
    e = 50
    return a + b + c + d + e

result = first_func()

#attempt 
a = 10

def first_func(b=20):
    c = 30
    value = second_func(b,c) #This first function is the second function, with values being assinged
    return value

def second_func(b,c,d=40): 
    e = 50
    return a + b + c + d + e

result = first_func()
print(result)

#attempt*
a = 10

def first_func(b=20):
    c = 30
    value = second_func() 
    return value

def second_func(b,c,d=40): 
    e = 50
    return a + b + c + d + e
result = first_func()
print(result)
# second_func() missing 2 required positional arguments: 'b' and 'c'
#the problem is that b and c are local values in first_func, 
# whereas a is global, d and e are local values in the seond_func

a = 10

def first_func(b=20):
    c = 30
    value = second_func(b,c) 
    return value

def second_func(b,c,d=40): 
    e = 50
    return a + b + c + d + e
result = first_func()
print(result)

#
a = 10

def first_func(b=20):
    c = 30
    value = second_func(b,c,d=42) 
    return value

def second_func(b,c,d=40): 
    e = 50
    return a + b + c + d + e
result = first_func()
print(result)

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}

def func(x): 
    x= {key.capitalize() for key in x}
    return x
fixed_1 = func (start_dict)
print (fixed_1)

def func_final(y):
    y = {key_name:val '%m/%d/%Y' for key_name in y}
    return y
fixed_2 = func_final(fixed_1)
print (fixed_2)


#attempt 2 
def fixer(x):
    x = {key_func(k).capitalize :val_func(v).strptime
     for k, v in x}
    return (x)

fx=fixer(start_dict)
print(fx)

#datetime function

x='2/23/1999'
from datetime import datetime 
x=datetime.strptime(x,'%m/%d/%Y').strftime('%Y-%m-%d')
print(x)



#attempt 3
from datetime import datetime

def fixer(x):
    fixed_dict = {k.capitalize() #key_func(k)
                  :datetime.strptime(v,'%m/%d/%Y').strftime('%Y-%m-%d') #val_func(v)
         for k, v in x.items()}
    return fixed_dict
fixed_dict = fixer(start_dict)
print(fixed_dict)

#attempt 4, fix the 0 in front of month
from datetime import datetime

def fixer(x):
    fixed_dict = {k.capitalize() #key_func(k)
                  :datetime.strptime(v,'%m/%d/%Y').strftime('%Y-%-m-%d') #val_func(v)
         for k, v in x.items()}
    return fixed_dict
fixed_dict = fixer(start_dict)
print(fixed_dict)


#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values
from numpy import mean, std

n = [1,2,3,4,5]
def stdizd(n):
    standardized_x_s = [(x - mean(n)) / std(n) for x in n]
    return standardized_x_s
standard_n = stdizd(n)
print(standard_n)



#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior
from numpy import median, absolute

n = [1,2,3,4,5]
def stdizd(n,mad=False):
    n_med = median(n)
    n_mean = mean(n)
    std_n = std(n)
    output = []
    for x in n:
        if mad:
            MAD = median (abs(x - n_med))
            madized = (x - n_med)/MAD
            output.append(madized)
        else:
            standardized_x_s = [(x - n_mean) /std_n]
            return standardized_x_s
        return output
 
standard_n = stdizd(n)
print(standard_n)       

standard_n = stdizd(n,True)
print(standard_n)



def stdizd(n, mad=False):
    n_med = median(n)  # Missing import statement for median, mean, and std functions
    n_mean = mean(n)  # Missing import statement for median, mean, and std functions
    std_n = std(n)  # Missing import statement for median, mean, and std functions
    output = []  # Indentation issue, this line should be inside the function

    for x in n:
        if mad:
            MAD = median(abs(n - n_med))  # abs(n - n_med) is incorrect, should be abs(x - n_med)
            madized = (x - n_med) / MAD
            output.append(madized)
        else:
            standardized_x_s = (x - n_mean) / std_n
            return standardized_x_s  # This return statement should be outside the loop and the if-else block
    return output  # This return statement should be outside the loop, inside the function

standard_n = stdizd(n)
print(standard_n)       

standard_n = stdizd(n, True)
print(standard_n)


#
from statistics import mean

n = [1, 2, 3, 4, 5]

def stdizd(n, use_modified_zscore=False):
    if use_modified_zscore:
        MAD = median([abs(x - median(n)) for x in n])
        standardized_x_s = [(x - mean(n)) / MAD for x in n]
    else:
        standardized_x_s = [(x - mean(n)) / std(n) for x in n]
    return standardized_x_s

standard_n = stdizd(n)
print(standard_n)  # Using standard z-score calculation

standard_n_modified = stdizd(n, use_modified_zscore=True)
print(standard_n_modified)  # Using modified z-score calculation

