class house:
  def color(self):
    print("This is red clour")
  def size(self):
    print("4 bhk flat")
class house1:
  def color(self):
    print("This is red clour")
  def size(self):
    print("4 bhk flat")
  def price(self):
    print("35 lakh")
h=house()
h.color()
h.size()
h1=house1()
h1.color()
h1.size()
h1.price()

class house:
  def color(self):
    print("This is red clour")
  def size(self):
    print("4 bhk flat")
class house1(house):
  def price(self):
    print("35 lakh")
h=house()
h.color()
h.size()
h1=house1()
h1.color()
h1.size()
h1.price()

class car:
  def __init__(self):
    print("This is car class")
class suzuki(car):
  def __init__(self):
    #super().__init__()
    print("This is suzuki class")
s=suzuki()
#operator overriding: is a situation when base class method is similar to child class method
# we can call base class method using super() keyword

class shape:
  def __init__(self,length,bredth):
    self.length=length
    self.bredth=bredth
  def area():
    print("This is shape Area")
class triangle(shape):
  def area(self):
    area=0.5*self.length*self.bredth
    print("Area of Triange=",area)
class rectangle(shape):
  def area(self):
    area=self.length*self.bredth
    print("Area of rectangle",area)
    
t=triangle(10,15)
t.area()
r=rectangle(10,5)
r.area()
