'''
DATE=29th NOV 2022
DAY= saturday
TOPIC= list
AUTHOR= nikhil
'''
p=[]
print(p,type(p))  #[] list
p=['paspuleti',22]
print(p,type(p)) #['nikhil',22] list
print(p[0],type(p[0])) #nikhil str
print(p[0],type(p[1])) #nikhil int
# print(p[2]) #indexerror:list index out of range
print(p[-1]) #22
c=None
print(c,type(c)) #None NoneType
r="hey"
# r[0]='H' #typeerror:"str" object does not support item assignment
k=[3,8.7,'paspuleti']
k[0]=5.3
k[-1]='kp'
print(k) #[5.3,8.7,'kp']
o=[2,4.3,'hi',[4,5]]
o.append(3)
print(o) #[2,4.3,'hi',[4,5],3]
o.clear()
print(o) #[]
g=[2,4,'hey']
j=g.copy()
print(j) #[2,4,'hey]
f=[2.5,4,'hello','']
print(f.count('')) #1
print(f.count(3)) #0
print(f.count('hello')) #1