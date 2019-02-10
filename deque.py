from collections import deque

numbers = deque()
print(len(numbers))
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)

print(numbers)
print(len(numbers))

x = numbers.popleft()
y = numbers.popleft()
z = numbers.popleft()
a = numbers.popleft()

print(x)
print(numbers)
print(len(numbers))