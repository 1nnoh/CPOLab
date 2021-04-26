# Lab1: Different approach for algorithms and data structure implementation

  *University : HDU*

  *Institute : ITMO joint institute*

  *Course : Computional Process Organization (Sping 2021)*

  *group members : Junhao Hou (s202320081)、 Yitian Xu (s202320082)*

  *laboratory work number： 2*

  *variant description： Dynamic array* 

##   Task division: 

    Junhao Hou: implementation and test of immutable dynamic array
    
    Yitian Xu: implementation and test of mutable dynamic array

## Description of assignment:

  Dynamic array (link)

• You can use the built-in list inside node with a fixed size

• You need to check that your implementation correctly works with None value

• You need to implement functions/methods for getting/setting value by index

• A user should specify growing factor

The growth factor is all about efficient memory usage and performance. How it works:

  (a) You have a chunk of memory. The chunk has a capacity (how many elements it can

contain) and length (how many elements it contains right now).

  (b) You need to add a new element, but capacity == length. You don’t have space

for a new element. What will we need to do?

    i. Allocate a new chunk of memory (in Python, usually, it looks like [None]*(capacity* growth_factor))
    ii. Copy data from the old chunk to the new chunk
    iii. Add a new element to the new chunk.




* Compare mutable and immutable implementation

  Objects of variable types do not need to be recreated when modified and do not waste memory space. Immedible type objects do not make efficient use of memory, but backtracking can be implemented, etc. 
  
  Implementation of two kinds of classes: object functions of immedible types are defined outside the class, and variable objects are defined inside the class.

## Test result

Mutable:

![test_mut](C:\Users\45539\Desktop\CPO\CPOLab\Lab1\src\pics\test_mut.png)

Immutable:

![test_imm](C:\Users\45539\Desktop\CPO\CPOLab\Lab1\src\pics\test_imm.png)

## Conclusion

The function implementation of the immutable type is outside the class, and only function declarations are available inside the class. When you modify a variable type, the memory address of the object does not change. The various functional functions that implement dynamic arrays make us find that the most difficult to handle is the empty object, and its judgment will directly affect the normal use of all functions.