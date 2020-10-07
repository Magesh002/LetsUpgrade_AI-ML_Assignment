"""
1. Range is a build-in function in python.
2. It is used to perform the action n times.
3. In python(2.x) we called as xrange.
4. Range takes mainly 3 arguments.
    4.1. Start: Integer will start from sequence of number will be return.
    4.2. Stop: Integer will stop before sequence of number will be return and its ends at stop-1.
    4.3. Step: It determine the increment between each value.
"""

for i in range(10):
    print(i, end=" ")

for i in range(11, 20):
    print(i, end=" ")

for i in range(21, 30, 2):
    print(i, end=" ")