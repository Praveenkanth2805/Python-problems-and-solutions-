#single inheritance

''' A <= B '''

#multilevel inheritance

''' A <= B <= C '''

#multiple inheritance

''' A , B <= C '''

#hirearchical inheritance

''' A => B , C '''

#multilevel inheritance
 #combination of  more then two type of inheritance

'''
                   A
                  / \
                 B   C
                 |   |
                 D - E
    
    OR
    
    A => B,C ; D,C <= E ; A <= B ; A <= B <= D

'''

#example

class college: #A
    cname = 'ABC'
    def display(self):
        print(f"it is a {s.cname} college")
        
class department( college ): #B
    cs = "computer science"
    def comp_sci(s):
        print(f"it is {s.cs} deparatment, 260+ students are studied in this department")

class pet(college): #C
    petname="Ganthimathi"
    def disp(s):
       print(f"I am the physical educational staff, my name is {s.petname}")

class staff (department):#D
    sname='Praveenkanth'
    def comp_staff(s):
        print(f"my name is {s.sname}, I am the {s.cs} department staff")


class student(staff,pet): #E
    def show(s):
        stud_name="sivakanthan"
        print(f"my name is {stud_name}. i am studied {s.cname} college, in {s.cs} departement, mystaff name is {s.sname} and my peteacher name is {s.petname}")

s = student()
s.display()
s.comp_sci()
s.comp_staff()
s.show()

p=pet()
p.disp()
