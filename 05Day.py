#list
marks=[1,2,3,4,5,6]
print(type(marks))
print(marks)
print(marks[0])
print(marks[:])

def app():
    for i in marks:
        print(marks[i-1])

app()

#methods of list
marks.append(2)
marks.sort()

#touple
tup=(1,2,3)
#unchangebale
print(tup)
print(tup[0])
import time
t=time.strftime('%H:%M:%S')
print(t)