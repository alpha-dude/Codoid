l= list(map(int,input("Enter the element: ").split(" "))) # Enter the number with spaces in-between
maximum = l[0]

# Iterating through the list of array
for i in range(1, len(l)):
# swapping the maximum number with minimum number
    if(l[i] > maximum):
        maximum = l[i]


print(maximum)
