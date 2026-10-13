class student:

    def __init__(self,name,roll_no):
        self.name= name
        self.roll_no= roll_no

    def display(self):    
        print("Name:", self.name)
        print("Roll no:", self.roll_no)

student1 = student("Manu", 101)
student1.display()

