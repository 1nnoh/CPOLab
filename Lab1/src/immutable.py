# coding=utf-8

import ctypes

class DynamicArray(object):
    def __init__(self, l=[]):
        self._len = 0  # Current array size
        self._capacity = 100  # Array capacity
        self._A = self._make_array(self._capacity)  # Open up space
        if len(l) >= self._capacity:  # Check if the current capacity is enough
            self._resize(2 * len(l))
        for i in range(len(l)):
            self._A[i] = l[i]
            self._len = len(l)

    def __iter__(self):
            return Next(self)

    def __eq__(self, other):
        if other is None:
            return False
        if size(other) != size(self):
            return False
        if type(other) != type(self):
            return False
        for i in range(size(other)):
            if self._A[i] != other._A[i]:
                return False
        return True

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._len):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

class Next:
    def __init__(self, dynamic_arr):
        self._A = dynamic_arr._A
        self._len = dynamic_arr._len
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self._len-1:
            x = self._A[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration

#Give the size of DA.
def size(n:DynamicArray):
    return n._len

#Add new element at the head.
def add_to_head(n:DynamicArray, new_element):   #new element is the value is going to be appended
    if n._len == n._capacity:    #to confirm if the current capacity is adequate.
        n._resize(2 * n._capacity)
    for j in range(n._len, 0, -1):
        n._A[j] = n._A[j-1]
    n._A[0] = new_element
    n._len += 1
    return n

#Add data at the tail.
def add_to_tail(n:DynamicArray, new_element):   #new element is the value is going to be appended
    if n._len == n._capacity:     #to confirm if the current capacity is adequate.
        n._resize(2 * n._capacity)
    n._A[n._len] = new_element
    n._len += 1
    return n

#To remove an element from the DA,
def remove(n:DynamicArray, r_element):
    l = []
    for i in range(size(n)):
        if i is not r_element:
            l.append(n._A[i])
    return DynamicArray(l)

#Transform the DA to a built-in list.
def to_list(n:DynamicArray) -> list:    #lst is a list,
    lst = []
    for e in n:
        lst.append(e)
    return lst

#Conversion from list to DA.
def from_list(lst:list):    #lst is a list,
    n = DynamicArray()
    if len(lst) >= n._capacity:     #to confirm if the current capacity is adequate.
        n._resize(2*len(lst))
    for i in range(len(lst)):
        n._A[i] = lst[i]
    n._len=len(lst)
    return n

#To find an element in Dynamic array, if it exists in the DA.
def find(n:DynamicArray, f_element):
    for e in n:
        if e is f_element:
            return True
    return False

#Filter data structrue.
def filter(n:DynamicArray, element):
    l = []
    for e in n:
        if e is not element:
            l.append(e)
    return DynamicArray(l)

#Map structure by speciﬁc function.
def map(n:DynamicArray, f):
    l = []
    for e in n:
        l.append(f(e))
    return DynamicArray(l)

#Reduce: process structure elements to build a return value by speciﬁc functions.
def reduce(n:DynamicArray, f, initial_state):
    state = initial_state
    cur = 0
    for i in range(n._len):
        state = f(state, n._A[cur])
        cur += 1
    return state

def mempty():
    return DynamicArray()

#Combine two DAs to one DA.
def mconcat(a:DynamicArray, b:DynamicArray):
    l1 = to_list(a)
    l2 = to_list(b)
    return DynamicArray(l1 + l2)


def iterator(lst:DynamicArray):
    if lst is not None:
        length=size(lst)
    else:
        length=0
    da = lst
    index=0

    def foo():
        nonlocal da
        nonlocal length
        nonlocal index
        if ( (da is None) | (index >= length)) : raise StopIteration
        tmp = da._A[index]
        index=index+1
        return tmp
    return foo


