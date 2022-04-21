import array as arr  
number = arr.array('i', [90, 26, 33, 653, 41])  
del number[2]                           # removing third element  
print(number)                           # Output: array('i', [1, 2, 3, 4])  