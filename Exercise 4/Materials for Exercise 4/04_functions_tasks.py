# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Andreas Schörgenhumer
Contact -- schoergenhumer@ml.jku.at
Date -- 27.07.2022

################################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
manuscript, no matter whether as a whole or in parts, no matter whether in
printed or in electronic form, requires explicit prior acceptance of the
authors.

################################################################################

Tasks for self-study. Try to solve these tasks on your own and compare your
solutions to the provided solutions file.
"""

#
# Task 1
#

# Write a function that divides two numbers and returns the result. The numbers
# should be taken as keyword arguments with defaults of 1.0 for both values.

def divide (x=1.0, y=1.0):                            #could work for lists only if you code divide(*my_list)
    return x / y

my_list = [12, 3]
my_dict = ["x": 7]

#(x=1, y=1) are keywords
#(1, 2) are positional

def mult(x, y)
     return x + y   #(also works for lists)


#
# Task 2
#

# Write a function that takes one argument that can be assumed to be a list. The
# function should add up the last two elements in the list, print the sum and
# append it at the end of the list without any return value (in-place update).
a = [1, 2, 3, 5]

def append_to_list(lst:list):
    sum = lst[-1] + lst[-2]       #defines what part of the list should be used
    print(sum)
    lst.append(sum)


#
# Task 3
#

# Write a function that takes two lists as input and creates a list of 2-tuples,
# where always the i-th elements of both lists are combined. If one list is
# longer than the other, the remaining elements are ignored. Do not use the
# existing function "zip".
a1 = [1, 2, 3]
a2 = [4, 5]

def zip_lists(list1: list, list2: list) -> list:
    return [(a[i],b[i]) for i in range(min(len(a), len(b)))]


#
# Task 4
#

# Write a function that takes an iterable of integers as input and returns their
# sum. If the iterable is empty, 0 should be returned. Do not use the existing
# function "sum".

def my_sum(inters):
    result = 0
    for i in inters:
        result += i
    return result

#my_sum(1, 2, 3)  #if my_sum is given as a list like this, we have to write def my_sum(*inters) for the first line

#
# Task 5
#

# Write a function that takes an iterable of any type as input and returns the
# length. If the iterable is empty, 0 should be returned. Do not use the
# existing function "len".

def my_len(iterable):
    count = 0
    for i in iterable:        #it would be better to write _ instead of i
        count +=1             #inters and iterables are different, hence the different codes
    return count


#
# Task 6
#

# Write a function that takes a list of integers as input, replaces all negative
# values with their positive/absolute values and returns this list. The function
# also has a boolean parameter which specifies if the replacement of the
# negative numbers should be done in-place, i.e., the changes are directly made
# on the input list, or if the replacement should be done in a new list, i.e.,
# the input list remains unchanged. By default, a copy should be returned.
# Otherwise, i.e., using in-place changes, nothing should be returned (None).
# Furthermore, the function should have a second parameter that specifies a set
# of negative values which should NOT be changed to positive values but instead
# should be excluded from the input list. By default, the negative numbers -1,
# -2 and -3 should be ignored.
a = [1, 2, -1, -5, 3, -4, -2, 0]


def filter_numbers(int_list, copy=True, values_to_ignore: set = None):
    if values_to_ignore is None:
        values_to_ignore = {-1, -2, -3}
    if copy:
        return [i * -1 if i <0 else i for i in int_list
                if i not in values_to_ignore]
    else:
        i = 0
        while i < len(int_list):
            val = int_list[i]
            if val in values_to_ignore:
                int_list.pop(i)
            else:
                int_list[i] = abs(val)
                i += 1

