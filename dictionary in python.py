#Qn 1: create first dictionary
#print keys,values,key and values
#Qn 2: create dictionary using dict() function
#use dict functions like pop, popitem, clear, copy

#Qn:1

d1={"name":"Praveenkanth", "age":20, "place":"Villupuram", "course":"CS"}

print(d1.keys())
print(d1.values())
print(d1.items())

#using loop way

for i in d1.keys():
    print(i)

for j in d1.values():
    print(j)

for i,j in d1.items():
    print(f"{i}:{j}")

#Qn:2

d2=dict(name="Arulaalan", age=20, place="Tiruvannamalai")
print(f"\nit is d2:{d2}")

'''d3=dict(d2)'''
d3=d2.copy()
d3.update({"course":"CS"})
d3["course id"]=214

print(f"\nit is copy of d2 dict and add course&id for make different\n{d3}")

d3.pop("course")
print(f"\nafter pop:{d3}")

d3.popitem()
print(f"\nafter popitem:{d3}")

d3.clear()
print(f"\nafter clear:{d3}")



















    
