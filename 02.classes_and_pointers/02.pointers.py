# without pointer
num1 = 11
num2 = num1
print("Before value is updated")
print("num1 =", num1)
print("num2 =", num2)
num1 = 22
print("After value is updated")
print("num1 =", num1)
print("num2 =", num2)

# with pointer
# both dict1 and dict2 point to the dictionary {'value' : 11} in memory
# without a pointer, {'value' : 11} would be no longer reachable and the memory would be released
dict1 = {'value':11} 
dict2 = dict1
print("Before value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)
dict1['value'] = 22
print("After value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)