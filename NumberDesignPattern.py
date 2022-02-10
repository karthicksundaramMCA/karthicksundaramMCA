########This file contains several number design patterns which are helpful for new programmers/developers.#########
n=int(input("Enter number for this pattern show: "))

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5
"""
n1=list(range(n))
del(n1[0]);
n1.insert(len(n1),len(n1)+1)
for each_element in n1:
    print(str(each_element) * each_element)
print()
print()
print()


"""
1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5
"""
n1=list(range(n))
del(n1[0]);
n1.insert(len(n1),len(n1)+1)
pattern_string=''
col=1
for row in n1:
    while(col<=row):
        pattern_string=pattern_string+''+str(col)
        col=col+1
    print(pattern_string)
print()
print()
print()

"""
1 1 1 1 
2 2 2 
3 3 
4 
"""
n1=list(range(n))
del(n1[0]);
n1.insert(len(n1),len(n1)+1)
for i in n1:
  print(str(i)*(len(n1)-(i-1)))
print()
print()
print()


  
"""
1 1 1 1 
2 2 2 
3 3 
4 
n=[1,2,3,4]
j=len(n)
for i in j:
    print(str(i)*j)
    j=j-1    
#both coding are same
n=[1,2,3,4]
j=len(n)
for i in n:
  print(str(i)*(len(n)-(i-1)))    
"""
"""=============================================================="""


"""
55555
5555
555
55
5
"""
#n=int(input("Enter number for this pattern show: "))
j=n
while(j>=0):
    print(str(n)*j)
    j=j-1
print()
print()
print()
    
"""
55555
4444
333
22
1
"""
#n=int(input("Enter number for this pattern show: "))
j=n
while(j>=0):
    print(str(j)*j)
    j=j-1
print()
print()
print()


"""
012345
01234
0123
012
01
"""
j=n

while(j>0):
    k=''
    r=range(j+1)
    for i in r:
      k=k+' '+str(i)
    print(k)
    j=j-1
print()
print()       
print()

    
"""
1
23
456
78910
"""
j=1
k=''
l=1
while(j<=n): 
    i=0
    k=''
    while(j>i):
    #for i in j:
        k=k+' '+str(l)
        #k=k+' '+str(int(j+i))
        i=i+1
        l=l+1
    j=j+1
    print(k)
print()
print()
print()


"""
1
3 2
6 5 4
10 9 8 7
"""
j=1
k=''
l=1
while(j<=n): 
    i=0
    k=''
    while(j>i):
    #for i in j:
        k=str(l)+' '+k
        #k=k+' '+str(int(j+i))
        i=i+1
        l=l+1
    j=j+1
    print(k)
print()
print()
print()


"""
1
2 3 4
5 6 7 8 9
"""
i=1 #Line Tracker
j=1 #Numbers to be displayed on each column
while(i<=n):
    l=1 #Column Tracker, used for printing j for each row.
    k='' #Temparoray variable used to print the numbers in a format.
    while(l<=i):
        k=k+' '+str(j)
        j=j+1
        l=l+1
    i=i+2
    print(k)
print()
print()
print()
 
    
"""
10
10 8
10 8 6 
10 8 6 4
10 8 6 4 2
Map, lambda can be used to this pattern 
"""   
import math
i=2
total_element=math.floor(n/2)
number_list=[]
while(i<=n):
    number_list.append(i)
    i=i+2
row=1
while(row<=total_element):
    position=total_element-1
    col=row
    pattern_string=''
    while(col>0 and row<=total_element):
        pattern_string=pattern_string+' '+str(number_list[position])
        position=position-1
        col=col-1
    row=row+1
    print(pattern_string)
