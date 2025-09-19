class Student:
    def __init__(self, name, dob, mark):
        self.name = name          
        self.mark = mark           
        self.dob = dob    

    def show_details(self):
        print(f"Name: {self.name}, Dob: {self.dob}, Marks: {self.mark}")

    def get_age(self):  
        age = 2025-int(self.dob[6:])
        print(f"Name: {self.name}, Dob: {self.dob}, age: {age}")


s1 = Student("Praveenkanth", "28-05-2005", 95)
s1.show_details()
s1.get_age()

