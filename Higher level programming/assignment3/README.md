# assignment 3 by Rosa (rnalsgaa)
# 21/09/2021

Last updated: 21/09/2021 11:20

## Task 2.1

### Prerequisites

To run the test, run

  $ python3 test_Array.py

in the terminal window. Print should look something like this:
  
  My nice string is ...
  My nice 2d string is ...
  My other nice 2d string is ...
  test_add OK
  test_sub OK
  ...
  test2d_add OK
  test2d OK
  test2d_eq OK
  ...

### Functionality

- Array is a class which can represent a 1-dimensional or 2-dimensional array
- Array objects can add, sub and multiply with same-shape arrays or a scalar
- Find smallest float in array

### Missing Functionality

- N-dimensional arrays are not implemented
- Theres will probably be errors if test_Array.py is slightly changed 
  because the program is not robust
- Program does not see difference between (3,2) and (2,3) arrays

### Usage

__add__
- Add two same-shape arrays element-wise
- Add array element-wise with scalar
__sub__
- Sub two same-shape arrays
- Sub array element-wise with scalar
__mul__
- Multiply two same-shape arrays eleemnt-wise
- Multiply array element-wise with scalar
__eq__
- Checks if two arrays are identical
is_equal
- Shows the user where an array has elements equal to another same-shape array or scalar
min_element
- Finds smallest float in array
