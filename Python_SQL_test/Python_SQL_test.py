# Answer to Question 1
def maximum_number(list1):
    a=list1[0]
    for i in range(1,len(list1)):
        if (list1[i]>a):
            a=list1[i]
    return a

# Answer to Question 2
def increase_list_container(prime_list,place):
        temp=[0]*(len(prime_list)*2)
        for a in range(place):
            temp[a]=prime_list[a]
        prime_list=temp
        return prime_list

    

def list_of_prime(x):
    prime_list=[0]*10
    place=0
    for i in range(2,x):
        prime=True
        for r in range(0,place):
            if(i%prime_list[r]==0):
                prime=False
                break
        if(prime):    
            prime_list[place]=i
            place+=1
            if(place==len(prime_list)):
                prime_list=increase_list_container(prime_list,place)
    return prime_list[:place]

# Answer to Question 3

def factorial(x):
    if (x==1):
        return x
    else:
        return factorial(x-1)*x
    
# Answer to Question 4

def list_merger(list_a, list_b):
    [a,b,c]=[0,0,0]
    list_c=[0]*(len(list_a)+len(list_b))
    while(a<len(list_a) and b<len(list_b)):
        if(list_a[a]<list_b[b]):
            list_c[c]=list_a[a]
            c+=1
            a+=1
        else:
            list_c[c]=list_b[b]
            c+=1
            b+=1
    if(a==len(list_a)):
        for i in range(b,len(list_b)):
            list_c[c]=list_b[i]
            c+=1
    else:
        for i in range(a,len(list_a)):
            list_c[c]=list_a[i]
            c+=1 
    return(list_c)

# Answer to question 5

import math

class Shape:
    def __init__(self, length, width,):
        self.length=length
        self.width=width
        
        def area(self):
            return self.length*self.width/2
        def perimeter(self):
            return math.sqrt(self.width*self.width+self.length*self.length)+self.width+self.length

class Rectangle(Shape):
    
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return self.length*2+self.width*2
    
class Circle(Shape):

    def area(self):
        return self.width/2*self.width/2*math.pi
    def perimeter(self):
        return self.width/2*math.pi
    
        
    