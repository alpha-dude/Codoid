string = "Python" # String goes here

char = str('s')

newstr = ""

for i in range(len(string)):
    if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
        newstr = newstr + char
    else:
        newstr = newstr + string[i]

print("\nOriginal String:", string)
print("New String:", newstr)
