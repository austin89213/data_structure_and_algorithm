# the function below is o(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)

# the function below actually is o(n^3)
# but we can simplify it as o(n2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
print_items(10)