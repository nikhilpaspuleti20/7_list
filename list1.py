'''
DATE=29th NOV 2022
DAY= saturday
TOPIC= list
AUTHOR= nikhil
'''
a=[15,20,25]
b=[30,35,40]
a.extend(b)
print(a) #[15,20,25,30,35,40]
b.extend(a)
print(b) #[30,35,40,15,20,25,30,35,40]
c='hey'
# print(c.index('w')) #valueerror:substring not found
k=[1,2,'read',[3]]
print(k.index(2)) #1
print(k.index([3])) #3
print(k.insert(1,'hi'))
print(k) #[1,'hi',2,'read',[3]]
l=[10,20,30]
l.pop()
print(l) #[10,20]
print(l.pop(1)) #20
h=['nikhil',5,25,3]
h.remove(3)
print(h) #['nikhil',5,25]
h.reverse()
print(h) #[25,5,'pooja']
u=[5,7,14,47,25,65]
u.sort()
print(u) #[5,7,14,25,47,65]
u.sort(reverse=False)
print(u) #[5,7,14,25,47,65]
u.sort(reverse=True)
print(u) #[65,47,25,14,7,5]