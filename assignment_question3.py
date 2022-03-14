list=[1,2,3,4,5,6,7,8,9]
ecount,ocount=0,0
for i in list:
    if i%2==0:
        ecount+=1
    else :
        ocount+=1
print("Number of even Numbers:",ecount)
print("Number of odd Numbers:",ocount)
