'''Problem:
    Write a Python program to find the maximum and minimum value in a dictionary.
Explanation:
    Use max() and min() with .values().

Test Cases:
    Case 1:
        {'a': 5, 'b': 9, 'c': 2}
    Output:
        Max = 9, Min = 2
    Case 2:
        {'x': 100, 'y': 500, 'z': 300}
    Output:
        Max = 500, Min = 100'''

d={'a': 5, 'b': 9, 'c': 2,'m':18,'p': 20 }
for i,j in d.items():
    print(f"{i}={j}")
#m=min(d.values())
print(f"\nMin={min(d.values())}, Max={max(d.values())}")
