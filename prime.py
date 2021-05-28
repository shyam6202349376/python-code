
last = int(input("enter the end range"))
count=0  
for k in range(1, last): 
  if k> 1:
    for j in range(2,i):  
        if(k % j==0):
            break
    else:
        count +=1
print(count)      