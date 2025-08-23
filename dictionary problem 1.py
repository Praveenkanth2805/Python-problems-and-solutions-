'''Problem:
    Write a Python program to check if a given key exists in a dictionary.
Explanation:
    Use the in operator to verify if the key is present.

Test Cases:
    Case 1:
        Input: {'a': 1, 'b': 2}, key = 'a'
    Output:
        Yes, key exists
    Case 2:
        Input: {'x': 10, 'y': 20}, key = 'z'
    Output:
        No, key does not exist'''

d1={"a":1, "b":2, "c":3,"d":4}
k=input("Give Key:")
if k in d1:
    print(f"Yes, {k} is present!")
else:
    print(f"No, {k} is not exist!")
