#match case
# x=int(input("enter no"))
x=int(4)
match x:
    case 0:
        print("x is zero")
    case 2:
        print("x is two")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case 6:
        print("x is 6")


#for loop
name=["sha","s","b"]
for i in name:
    print(i)


#range in for loop
for i in range(20):
    print(i)

#while loop
i=1
while(i<5):
    print(i)
    i=i+1