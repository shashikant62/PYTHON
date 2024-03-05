#internal working of python
a=[1,2,3]
b=a
print(a)
print(b)
a[0]=44
print(a)
print(b)

#case-2
a=[1,2,3]
b=a[:] #copy created
print(a)
print(b)
a[0]=44
print(a)
print(b)