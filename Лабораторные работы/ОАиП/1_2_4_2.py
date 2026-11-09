name = input()
age = int(input())
temp = 0
print(f"name = {type(name)}\nage = {type(age)}")
temp = age; age = name; name = temp;
print(f"name = {type(name)}\nage = {type(age)}")