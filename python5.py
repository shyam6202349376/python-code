str = str(input("enter number "))
list=str.split(",")
num = len(list)
list.sort()
  
if num % 2 == 0:
    median1 = list[num//2]
    median2 = list[num//2 - 1]
    median = (median1 + median2)/2
else:
    median = list[num//2]
print(median)