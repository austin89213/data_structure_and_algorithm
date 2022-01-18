# the function below actually is o(2n), but the constants don't matter
# so we still call it O(n)

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)