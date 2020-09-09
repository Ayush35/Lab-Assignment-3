
list = ['abc','xyz','aba','1221'] #sample list
num=0                               #counter
for i in list:                      # i will point in every element at a time in the list
    if len(i)>1 and i[0] == i[-1] :  #condition 
        num= num+1                  #counter incremented if condition is true   
           

print(num)                          #here's the answer to be printed
