def isPronicNumber(num):    #Function to check whether it is pronic number or not
    flag = False;    
        
    for j in range(1, num+1):    

        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
       
print("Pronic numbers between 1 and 100: ") #Displays pronic numbers between 1 and 100      
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i) 
