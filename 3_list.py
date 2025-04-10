a = ["aeroplane", "bus", "car", "bus", "aeroplane"]
b = a.copy()
print(b)
a.reverse()
print(b)
if a == b:
    print(f"it is a palindrome{b}")
else:
    print(f"it is not a plindrome{b}")