# assignment 3 by Rosa (rnalsgaa)
# 20/09/2021

from typing import Type # this was automatically implemented so ill let it stay

class Array:


    def __init__(self, shape, *values):
        """
        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        self._ROWS = shape[0]
        if len(shape) > 1:
                # 2d array
                self._COL = shape[1]
        else:
            self._COL = 1
        self._array = [None]*self._ROWS
        # Check if the values are of valid type
        if Array.isLegalType(values) and len(values) == self._ROWS*self._COL:
            if self._COL > 1:
                # 2d array
                v = 0
                i = 0
                j = 0
                while i < self._ROWS:
                    col = [0.]*self._COL
                    while j < self._COL:
                        # If values are not of same type all are converted to float
                        col[j] = float(values[v])
                        v += 1
                        j += 1
                    self._array[i] = col
                    i += 1
                    j = 0
            else:
                # 1d array
                for i in range( len(self._array)):
                    self._array[i] = float(values[i])
        else:
            raise ValueError("Array contains non-floatable values or shape mismatch occured ")

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return str(self._array)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        # check that the method supports the given arguments (check for data type and shape of array)
        if Array.isLegalType(other):
            flat_array = Array.flat_array(self)
            if isinstance(other, list):
                # legge sammen n-dimensjon array med n-dimensjon array
                if len(other) == len(flat_array):
                    i = 0
                    while i < len(flat_array):
                        flat_array[i]+=other[i]
                        i += 1
                    return flat_array
            else:
                # sum scalar values
                i = 0
                while i < len(flat_array):
                    flat_array[i]+=other
                    i += 1
                return flat_array
        return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        # check that the method supports the given arguments (check for data type and shape of array)
        if Array.isLegalType(other):
            flat_array = Array.flat_array(self)
            if isinstance(other, list):
                # sub array with array
                if len(other) == len(flat_array):
                    i = 0
                    while i < len(flat_array):
                        flat_array[i]-=other[i]
                        i += 1
                    return flat_array
            else:
                # sub array with scalar
                i = 0
                while i < len(flat_array):
                    flat_array[i]-=other
                    i += 1
                return flat_array
        return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # check that the method supports the given arguments (check for data type and shape of array)
        if Array.isLegalType(other):
            if isinstance(other, list):
                # legge sammen n-dimensjon array med n-dimensjon array
                if len(other) == self._ROWS:
                    i = 0
                    while i < self._ROWS:
                        self._array[i]*=other[i]
                        i += 1
                    return self._array
            else:
                # sum scalar values
                i = 0
                while i < self._ROWS:
                    self._array[i]*=other
                    i += 1
                return self._array
        return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        isEqual = True
        if Array.isLegalType(other):
            flat_array = Array.flat_array(self)
            # check array shape
            if len(other) == len(flat_array):
                # compare each element
                for i in range( len(flat_array) ):
                    if not other[i] == flat_array[i]:
                        isEqual = False
                return isEqual
        return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        flat_array = Array.flat_array(self)
        identicalness = [False]*len(flat_array)
        if isinstance(other, (Array,list)):
            # check if equal shape
            if len(other) == self._ROWS*self._COL:
                for i in range( len(identicalness) ):
                    if flat_array[i] == other[i]:
                        identicalness[i] = True
            else:
                raise ValueError
        elif isinstance(other, (float, int)):
            # we have a scalar
            for i in range ( len(identicalness) ):
                if flat_array[i] == other:
                    identicalness[i] = True
        else:
            # input is neither array nor number
            return TypeError
        return identicalness

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        min = None
        for element in self._array:
            if min == None:
                min = element
            else:
                if element < min:
                    min = element
        return float(min)

    def __getitem__(self ,item):
        # this function is copied from the assignment example
        """Returns value of item in array.
        Args:
            item (int): Index of value to return.
        Returns:
            value: Value of the given item.
        """
        return self._array[item]

    def len(self, array):
        """Finds length of an Array
        Args:
            array (Array of any type): The array to count elements of
        Returns:
            int: The length of the array
        """
        len = 0
        for _ in array:
            len += 1
        return len

    def isLegalType(other):
        # Implemented this function to check list, Array and tuple type
        #   containers to check if they consist of int, float or bool type
        """Checks elements in container
        Args:
            other (list of any type or value): The thing to check.
        Legal Types:
            int, float, bool
        Returns:
            bool: True if all elements are of Legal Type. False otherwise.
        """
        legalTypes = [int, float, bool]
        if isinstance(other, (list, Array, tuple)):
            for element in other:
                if type(element) not in legalTypes:
                    return False
        else:
            if type(other) not in legalTypes:
                return False
        return True

    def flat_array(self):
        """Flattens the 2-dimensional array of values into a 1- dimensional array.
        Returns:
            list: flat list of array values.
        """
        if self._COL > 1:
            # 2d array
            flat_array = [0.]*self._ROWS*self._COL
            i = 0
            for row in self._array:
                for item in row:
                    flat_array[i] = item
                    i += 1
            return flat_array

        else:
            # already flat
            return self._array