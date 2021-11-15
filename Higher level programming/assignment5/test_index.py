venue = "DH 504"
slice = venue[-3:]
if (slice.isnumeric()):
    print(slice+" is numeric")
else:
    print(slice+" is not numeric")