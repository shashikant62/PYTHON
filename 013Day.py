# INTERNAL WORKING OF PY
#datatype gives to memory not a variable score(variable)->3(mem)
#python take ref_count in internal meomary 
import copy
#case-1 refrence cahnge
mylistone=[1,2,3]
mylisttwo=mylistone
print(mylistone)
print(mylisttwo)
mylistone='kabir'
print(mylistone)
print(mylisttwo)
mylistone=[1,2,3]
mylistone[0]=33
print(mylistone)
print(mylisttwo)

print("-----------------------------------")
#case-2 
l1=[1,2,3]
l2=l1
print(l1)
print(l2)
l1[0]=44
print(l1)
print(l2)

print("-----------------------------------")
#case-3
h1=[1,2,3]
h2=h1[:] #Create copy of thise
print(h1)
print(h2)
h1[0]=66
print(h1)
print(h2)

h3=[1,2,[3,2]]
h4=copy.deepcopy(h3)
print(h4)

print("-----------------------------------")
#case-4
m=10
n=m
print(n==m)
print(m is n)
n1=[1,2,3]
m1=[1,2,3]
print(n1==m1)
print(m1 is n1)