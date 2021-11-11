# Oblig 1
# 16/9/2021
# Erlend Lyra og Rosa

"""
Oppgave 1a: Teque pseudokode

proc push_front(x) do
    a <- put x in front

proc push_middle(x) do
    a <- put x at index |a| / 2

proc push_back(x) do
    a <- add x at the end

proc get(i) do
    return a[i]

"""

# Oppgave 1b: Teque i python
def push_front(x):
    array.insert(0,x)

def push_middle(x):
    middle_index=int( (len(array)+1) / 2 )
    array.insert(middle_index,x)

def push_back(x):
    array.append(x)

def get(i):
    return array[i]

array=[] # create array
count=int(input())

for _ in range(count):
    inp=list( input() ) # using a mutable type instead of string

    # extract value from input
    i=-1
    value = ""
    while inp[i] != ' ':
        value=inp[i]+value
        i-=1
    value=int(value)

    # execute command from input
    if inp[0] == 'g':
        # do get()
        print(get(value))
    else:
        if inp[5] == 'f':
            # do push_front()
            push_front(value)
        else:
            if inp[5] == 'm':
                # do push_middle()
                push_middle(value)
            else:
                # do push_back()
                push_back(value)


"""
Oppgave 1c: Teque kjoeretidsanalyse

If not other specified,
info collected from website
https://wiki.python.org/moin/TimeComplexity

- push_back
calls the operation .append(x) once,
which has worst case time-complexity O(1)

- push_front
calls the operation .insert(i,x) once,
which has worst case time-complexity O(n)

- push_middle
first line in block does arithmetic operations
and gets length. Getting length has time-complexity 
O(1). Second line calls the operation .insert(i,x) once.
Time-complexity is O(n)

- get
does index accessing once, which has time-complexity O(1)

----------------------------------------------------------------------------

Oppgave 1d: Teque kjoeretidsanalyse ved liten N

In most cases the time-complexity of an unlimited N gives
correct image of the time-complexity of an algorithm.
But if we already know that N is limited, we might see that a
generally "slower" algorithm in means of time-complexity
acts quicker than a "faster" algortihm. Thats because it
takes time for a function of a "fast" algorithm to develop its curve.
If a function of a "slower" algorithm develops faster
in the beginning, we can use this to our advantage.

"""