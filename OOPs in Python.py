#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Class and object or instance declaration:


# In[3]:


class Student:
    roll=""
    cgpa=""
    city=""
    
Afia=Student()
print(isinstance(Afia,Student))
Afia.roll=1059
Afia.cgpa=3.89
Afia.city="Dhaka"
print(f"Roll:{Afia.roll} , Cgpa:{Afia.cgpa} and City:{Afia.city}")


# In[4]:


#Declaring method(function):


# In[5]:


class Student:
    roll=""
    cgpa=""
    city=""
    def display(self):
        print(f"Roll:{self.roll} , Cgpa:{self.cgpa} and City:{self.city}")
    
Afia=Student()
print(isinstance(Afia,Student))
Afia.roll=1059
Afia.cgpa=3.89
Afia.city="Dhaka"
Afia.display()


# In[1]:


class Student:
    roll=""
    cgpa=""
    city=""
    def setValue(self,roll,cgpa,city):
        self.roll=roll
        self.cgpa=cgpa
        self.city=city
    def display(self):
        print(f"Roll:{self.roll} , Cgpa:{self.cgpa} and City:{self.city}")
    
Afia=Student()
print(isinstance(Afia,Student))
Afia.setValue(1059,3.89,"Dhaka")
Afia.display()


# In[3]:


#constructor: It is special type of function or method that dont need to call. We can pass parameter when we are building the object.


# In[ ]:


class Student:
    roll=""
    cgpa=""
    city=""
    def __init__(self,roll,cgpa,city):
        self.roll=roll
        self.cgpa=cgpa
        self.city=city
    def display(self):
        print(f"Roll:{self.roll} , Cgpa:{self.cgpa} and City:{self.city}")
    
Afia=Student(1059,3.9,"Dhaka")
print(isinstance(Afia,Student))

Afia.display()


# In[5]:


#Exercise:
class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_area(self):
        area=0.5*self.base*self.height
        print(f"Area of the triangle is {area}")
        
        
t1=triangle(10,20)
t2=triangle(20,30)
t1.calculate_area()
t2.calculate_area()


# In[6]:


#inheritance:


# In[10]:


class Phone:
    def call(self):
        print("Please call me")
    def message(self):
        print("Please message me")
        
class Samsung:
    def call(self):
        print("Please call me")
    def message(self):
        print("Please message me")
    def photo(self):
        print("Please take a photo")
        
p1=Phone()
p1.call()
p1.message()

s1=Samsung()
s1.call()
s1.message()
s1.photo()


# In[11]:


# We can do the above code by using inheritance


# In[15]:


class Phone:
    def call(self):
        print("Please call me")
    def message(self):
        print("Please message me")
        
class Samsung(Phone):
    
    def photo(self):
        print("Please take a photo")
        
p1=Phone()
p1.call()
p1.message()

s1=Samsung()
s1.call()
s1.message()
s1.photo()
print(issubclass(Samsung,Phone))


# In[14]:


class Phone:
    def call(self):
        print("Please call me")
    def message(self):
        print("Please message me")
        
class Samsung(Phone):
    
    def photo(self):
        pass
       
        
p1=Phone()
p1.call()
p1.message()

s1=Samsung()
s1.call()
s1.message()


#note: Use the pass keyword when you do not want to add any other properties or methods to the class.


# In[1]:


#method overriding:Using same method several time is known as method overriding


# In[4]:


class Phone:
    def __init__(self):
        print("I am in phone class")
    
    
class Samsung(Phone):
    def __init__(self):
     print("I am in Samsung class")
s1=Samsung()


# In[5]:


# To use the method of super class 


# In[16]:


class Phone:
    def __init__(self):
        print("I am in phone class")
    
    
class Samsung(Phone):
    
          def __init__(self):
            super().__init__()
            print("I am in Samsung class")
s1=Samsung()


# In[18]:


class phone:
    def __init__(self):
        print("I am in phone class")
        
class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I am in samsung class")
        
s1=samsung()


# In[20]:


class Shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    
class Triangle(Shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print("The area of the Triangle is=",area)
    
class Rectangle(Shape):
    def area(self):
        area=self.dim1*self.dim2
        print("The area of the Rectangle is=",area)
        
t1=Triangle(20,30)
t1.area()

t2=Rectangle(20,30)
t2.area()


# In[1]:


#Multilevel inheritance


# In[3]:


class A:
    def display1(self):
        print("I am in class A")
        
class B(A):
    def display2(self):
        print("I am in class B")
        
class C(B):
    def display3(self):
        print("I am in class C")
        
        
obj=C()
obj.display1()
obj.display2()
obj.display3()
        


# In[4]:


class A:
    def display1(self):
        print("I am in class A")
        
class B(A):
    def display2(self):
        print("I am in class B")
        
class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am in class C")
        
        
obj=C()

obj.display3()
        


# In[5]:


#Multiple inheritance:


# In[6]:


class A:
    def display1(self):
        print("I am in class A")
        
class B:
    def display2(self):
        print("I am in class B")
        
class C(A,B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am in class C")
        
        
obj=C()

obj.display3()
        


# In[7]:


class A:
    def display(self):
        print("I am in class A")
        
class B:
    def display(self):
        print("I am in class B")
        
class C(A,B):
    def display(self):
       
        print("I am in class C")
        
        
obj=C()

obj.display()
        


# In[11]:


class A:
    def display(self):
        print("I am in class A")
        
class B:
    def display(self):
        print("I am in class B")
        
class C(A,B):
    
        pass

        
        
obj=C()

obj.display()
        


# In[12]:


#Abstraction:


# In[21]:


from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod   
    def area(self):
        pass
    
class Triangle(Shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print("The area of the Triangle is=",area)
    
class Rectangle(Shape):
    def area(self):
        area=self.dim1*self.dim2
        print("The area of the Rectangle is=",area)
        

        
t1=Triangle(20,30)
t1.area()

t2=Rectangle(20,30)
t2.area()


# In[2]:


#Polymorphism


# In[3]:


#built in function
print(len("Afia Alom Chumki"))
print(len([10,20,50]))


# In[4]:


#user defined polymorphism


def add(x,y,z=0):
    return x+y+z

print(add(2,3))

print(add(2,4,6))


# In[ ]:




