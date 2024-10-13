first = int(input())
second = int(input())
third = int(input())
if first == second and second == third:
    print(3)
elif first == second or third == first or third == second:
    print(2)
else:
    print(0)
