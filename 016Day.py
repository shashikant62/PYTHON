#LIST(mutable)
li=['a','b','c','d','e']
print(li[-1])
print(li.pop())
print(li.insert(5,'k'))
print(li)

a=[x**2 for x in range(10)]
print(a)
print('---------------------------------')

#DICTIONARY(mutable)
dic={"a":"r1","b":"r2","c":"r3"}
print(dic.get('a'))
dic['a']='p1'
print(dic)

for i in dic:
    print(dic.get(i),"-",i,"-",dic[i])

for key ,value in dic.items():
    print(key,"-",value)

dic.pop('b')
print(dic)
dic.popitem()
print(dic)

squed_num={x:x**2 for x in range (6)}
print(squed_num)

#TOUPLE(immutable)

tea=('a','b','c')
print(tea[0])
print(tea)
print(len(tea))
print(tea)

(a1,a2,a3)=tea
print(a1)