"""Suraj Prathik Kumar
   2016101"""
def recursive_sum(n):
    l=len(str(n))
    sum=0
    for i in range(l):
        m=int(n)%10
        sum=sum+m
        n=int(n)/10
    if sum<10:
        return sum
    elif sum==0:
        return sum
    else:
        yo=sum
        return recursive_sum(yo)

    
