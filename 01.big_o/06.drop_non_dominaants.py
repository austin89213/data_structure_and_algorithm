# the function below actually is o(n^2 + n)
# but we can simplify it as o(n2)
def print_items(n):
    for i in range(n):
        for j in range(n):
    for k in range(n):
        print(i,j,k)
print_items(10)