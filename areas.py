class Shape:
  def __init__(self,name):
    self.name =name
  def calculate_area(self):
    pass
class Rectangle(Shape):
  def __init__(self,name,length,width):
    super().__init__(name)
    self.length =length
    self.width =width
  def calculate_area(self):
    return self.length*self.width
class Triangle(Shape):
  def __init__(self,name,base,height):
    super().__init__(name)
    self.base =base
    self.height =height
  def calculate_area(self):
    return 0.5*self.base*self.height
class Circle(Shape):
  def __init__(self,name,radius):
    super().__init__(name)
    self.radius =radius
  def calculate_area(self):
    return 3.14*self.radius*self.radius
rectangle =Rectangle("rectangle",10,9)
triangle =Triangle("triangle",7,44)
circle =Circle("circle",2)
shapes =[rectangle,triangle,circle]

for shape in shapes:
  area =shape.calculate_area()
  print(f"name:{shape.name}\n area:{area:.2f}")


