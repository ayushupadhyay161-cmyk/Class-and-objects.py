# Question 1 :Student Info Create a Student class with name, roll_no, marks. Create 3 objects and print their details using a method.

class Student():
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks 
    
    def hello(self):
        print("Hello", self.name, "your rollno. is", self.rollno, "and your score is:", self.marks)    
    
s1 = Student("Yash", 50, 89)
s1.hello()        

s2 = Student("Nitesh", 30, 54)
s2.hello()

s3 = Student("Prem", 45, 92)
s3.hello()



# Question 2 : 2. Rectangle Class Rectangle(length, breadth) Methods: area(), perimeter()

class Rectangle():
    def __init__(self, length, bredth):
        self.length = length 
        self.bredth = bredth 

    def lb_area(self):
        return self.length*self.bredth

    def lb_perimeter(self):
        return 2 * (self.length+self.bredth)    
    
lb1 = Rectangle(10, 20)
print("Area is :", lb1.lb_area())
print("Perimeter is :", lb1.lb_perimeter())



# Question 3 : 3. Circle Class Circle(radius) Methods: area(), circumference()

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def c_area(self):
        return math.pi * (self.radius ** 2)
    def c_circumference(self):
        return 2 * math.pi * self.radius   
r1 = Circle(10)
print("Area is :", r1.c_area())
print("Perimeter is :", r1.c_circumference())
r2 = Circle(5)
print("Area is :", r2.c_area())
print("Perimeter is :", r2.c_circumference())



# Question 4 : 4. Bank Account (basic) Class BankAccount(name, acc_no, balance) Methods: deposit(amount), withdraw(amount), show_balance().

class Account:
    def __init__(self, name, bal, acc):
        self.name = name 
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print(self.name, "your total balance = ", self.get_balance())
            
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print(self.name, "your total balance = ", self.get_balance())
            
    def get_balance(self):
        return self.balance
            
acc1 = Account("Ayush", 100000, 123456)       
acc1.credit(20000)
acc1.debit(500)

