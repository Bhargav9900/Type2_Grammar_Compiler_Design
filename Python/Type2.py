"""
@author: bhargav
"""
print("Bhargav Bechara")
num=int(input("Enter number of lines in grammar: "))

li=[]

for i in range(0,num):
    print("Enter",end=" ")
    print(i+1,end=" ")
    print("Rule",end=" ")
    gr=input()
    li.append(gr)
#print(li)

left_side=[]

for i in range(0,num):
    st=li[i].split('->')
    left_side.append(st[0])
    
#print(left_side)
c=0
for i in left_side:
    if((not i.isupper()) or (len(i)>1)):
        c=c+1
        
if c==0:
    print("Given grammar is type-2")
else:
    print("Give grammar is not type-2")
