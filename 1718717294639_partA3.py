t1=(1,2,5,7,9,2,4,6,8,10)
print("Tuple 1:",t1)
t2=(11,13,15)
print(f"Tuple 2:{t2}")
print("After slicing")
n=int(len(t1)/2)
print(t1[:n])
print(t1[n:])
l1=list()
for i in t1 :
    if i%2==0 :
        l1.append(i)
    tuple_even=tuple(l1)
print(f"Even numbers :{tuple_even}")
t3=t1+t2
print(f"Tuple 3 :{t3}")
print(f"Maximum value :{max(t3)}")
print(f"Minimum value :{min(t3)}")