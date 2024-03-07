#loops
#for loop
ap=["a",'b','c']
for i in ap:
 print(i)

n=10
for j in range(n):
 print(j)

#cout positive num
# num=int(input("How many roses?: "))
num=10
print(type(num))
cout=0
for k in range(num):
 if(k%2==0):
  cout=cout+1
 
print(cout)

#sum of even num
ans=0
for k in range(num+1):
 if(k%2==0):
  ans=k+ans
print(ans)

#multiplication table
# multy=2
# while(multy<=20):
#  ans=ans*2
#  print("multification=",multy)