# assignment 3 by Rosa (rnalsgaa)
# 20/09/2021

from Array import Array

# task 3.2 - Tests for 1D arrays
def test_str():
    # test __str__
    a = Array((3,), 9, True, True)
    b = Array((2,2), 1, 2, 3, 4)
    c = Array((3,4), True, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    print("My nice string is", a)
    print("My nice 2d string is\n"+str(b))
    print("My other nice 2d string is\n"+str(c))

def test_add():
    # test addition
    a = Array((3,), True, False, 3)
    assert a.__add__([1.2, 1, 1]) == [2.2, 1.0, 4.0]
    assert a.__add__(10) == [12.2, 11., 14.]
    assert a.__add__("Rosa") == NotImplemented
    print("test_add OK")

def test_sub():
    # test subtraction
    a = Array((3,), True, False, 3)
    assert a.__sub__([1, 1, 1]) == [0., -1., 2.]
    assert a.__sub__(0.1) == [-0.1, -1.1, 1.9]
    assert a.__sub__("to") == NotImplemented
    print("test_sub OK")

def test_mul():
    # test multiplication
    a = Array((3,), True, False, 3)
    assert a.__mul__([1,1.0,2]) == [1., 0., 6.]
    assert a.__mul__(10) == [10., 0., 60.]
    assert a.__mul__("10") == NotImplemented
    print("test_mul OK")

def test_eq():
    # test __eq__
    a = Array((3,), True, False, 3)
    assert a.__eq__([1., 0., 3]) == True
    assert a.__eq__([1., 0., 3.1,]) == False
    assert a.__eq__(["ja"]) == False
    assert a.__eq__([1., 0., "3"]) == False
    print("test_eq OK")

def test_is_equal():
    # test is_equal
    a = Array((3,), True, False, 3)
    assert a.is_equal(1.) == [True, False, False]
    assert a.is_equal([1., 0., 3.]) == [True, True, True]
    assert a.is_equal([2., 3., 4.]) == [False, False, False]
    print("test_is_equal OK")

def test_min_element():
    # test find smallest element
    a = Array((3,), True, False, 3)
    b = Array((4,), 5, 10, 2, 87)
    assert a.min_element() == 0.
    assert b.min_element() == 2.
    print("test min_element OK")


def test_isLegalType():
    # test isLegalType
    homo_array = Array((3,), 2., 2., 2.)
    assert Array.isLegalType(homo_array) == True
    try:
        not_homo_array = Array((3,), 2., "ja", True)
    except ValueError as valueError:
        # if we get here everything happened as planned
        print("test_isLegalType OK")

# calling test functions for 1d array
test_str()
test_add()
test_sub()
test_mul()
test_eq()
test_is_equal()
test_min_element()
test_isLegalType()

# task 3.3 - Tests for 2D arrays
def test2d_add():
    # test add for 2d array
    a = Array((2,2), 1, 2, 3, 4)
    print(a.__add__([0.1, 0.2, 0.3, 0.4]))
    assert a.__add__([0.1, 0.2, 0.3, 0.4]) == [1.1, 2.2, 3.3, 4.4]
    print("test2d_add OK")

def test2d_sub():
    # test sub for 2d array
    a = Array((2,2), 1, 2, 3, 4)
    assert a.__sub__([1., 1., 1., 1.]) == [0., 1., 2., 3.]
    print("test2d_sub OK")

def test2d_eq():
    # test __eq__ for 2d array
    a = Array((2,2), 1, 2, 3, 4)
    assert a.__eq__([1., 2., 3., 4.]) == True
    print("test2d_eq OK")

def test2d_is_equal():
    # test is_equal for 2d array
    a = Array((2,2), 1, 2, 3, 4)
    assert a.is_equal([1., 2., 1., 4.]) == [True, True, False, True]
    print("test2d_is_equal OK")

def test_flat_array():
    a = Array((3,), True, False, 3)
    b = Array((3,2), 1, 2, 3, 4, 5 ,6)
    print("My flat 1d array:", a.flat_array())
    print("My flat 2d array:", b.flat_array())

# calling test functions for 2d array
test_flat_array()
test2d_add()
test2d_sub()
test2d_eq()
test2d_is_equal()