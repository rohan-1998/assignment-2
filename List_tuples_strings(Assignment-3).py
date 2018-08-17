#lists
#Question 1
a=int(input("enter the no of elements"))
b=[]
for i in range(a):
    c=input("enter the element")
    b.append(c)
print(b)

#Question 2
d=['google','apple','facebook','microsoft','tesla']
b.extend(d)
print(b)

#Question 3
f=input("Enter the element to be counted in list")
print(b.count(f))

#Question 4
g=int(input("Enter the number of elements"))
h=[]
for i in range(g):
      c=int(input("Enter the number"))
      h.append(c)
h.sort()
print(h)

#Question 5
i=[3,2,1]
j=[7,5,6]
c=i+j
c.sort()
print(c)

#Question 6
even=0
odd=0
a=[1,2,3,4,4,5,5,6,6,6,6,3,4,4,8]
for i in range(len(a)):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("number of odd numbers in list",odd)
print("number of even numbers in list",even)

#optional
#stack(LIFO)
a=["ram","sham"]
b="rohan"
print(a)
print("pushing the element in stack")
a.append(b)
print(a)
print("poping the element from the list")
print(a.pop())
print(a)
#Queue(FIFO)
a=["ram","sham"]
b="rohan"
print(a)
print("pushing the element in list")
a.append(b)
print(a)
print("poping the  first element form the list")
print(a.pop(0))
print(a)


#tuples
#topic not covered


#strings
#Question 1
a=input("Enter the string in lowercase")
print(a)
print("converted into uppercase")
print(a.upper())

#Question 2
a=input("Enter the string")
print(a.isdigit())

#Question 3
b="Hello World"
print(b.replace("World","Rohan"))


