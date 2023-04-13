a = [[1, 3, 2, 9], [4, 0, 6, 5], [9, 1, 2, 8]]  # Matrix a
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]  # Matrix b

nra = len(a)   # No of rows in a
nca = len(a[0])  # No of columns in a
nrb = len(b)    # No of rows in b
ncb = len(b[0])  # No of columns in b

c = []  # empty list for result
d = []  # empty list for single row result


if (nra == nrb and nca == ncb):   # Checking that matrix addition is possible or not

    for i in range(len(a)):  # Looping on number of list
        for j in range(len(a[0])):  # Looping on number of elements in a single list
            d.append(a[i][j] + b[i][j])  # adding items in a d
        c.append(d)  # adding list d in c
        d = []  # Cleared d  for the next row

    for i in range(len(c)):  # Looping on number of list in c (for print final matrix)
        for j in range(len(c[0])):  # Looping on number of elements in a single c
            print('{: ^5}'.format(c[i][j]), end="")  # formatting and Printing single Row
        print()  # Line break after every row

else:  # If the matrix addition is not possible
    print("Matrix addition is not possible")
